import base64
import logging
from itertools import cycle
from typing import Dict, List, AsyncGenerator

import httpx
from fastapi import HTTPException

from doclearn.config import Config

logger = logging.getLogger(__name__)

# Configuração e utilitários
token_cycle = cycle(Config.tokens)


def get_next_token() -> str:
    return next(token_cycle)


async def get_github_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient() as client:
        yield client


# Funções de requisição
async def make_github_request(client: httpx.AsyncClient, url: str) -> httpx.Response:
    for _ in range(len(Config.tokens)):
        token = get_next_token()
        headers = {"Authorization": f"token {token}"} if token else {}

        response = await client.get(url, headers=headers)
        if response.status_code != 403:  # Não é um erro de limite de taxa
            return response

        logger.warning(
            "Rate limit atingido para o token atual. Alternando para o próximo token."
        )

    raise HTTPException(
        status_code=429, detail="Limite de taxa excedido para todos os tokens"
    )


async def fetch_markdown_files(
    client: httpx.AsyncClient, owner: str, repo: str, path: str = "", ref: str = "main"
) -> List[Dict]:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={ref}"

    logger.info(f"Buscando arquivos markdown de {url}")
    response = await make_github_request(client, url)
    response.raise_for_status()

    files = response.json()
    md_files = []

    for file in files:
        if file["type"] == "dir":
            logger.info(f"Entrando no diretório: {file['path']}")
            md_files.extend(
                await fetch_markdown_files(client, owner, repo, file["path"], ref)
            )
        elif file["name"].endswith(".md"):
            md_files.append(file)

    logger.info(f"Total de arquivos markdown encontrados: {len(md_files)}")
    return md_files


async def fetch_file_content(
    client: httpx.AsyncClient, owner: str, repo: str, file_path: str, ref: str = "main"
) -> str:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={ref}"

    logger.info(f"Buscando conteúdo do arquivo {file_path}")
    response = await make_github_request(client, url)
    if response.status_code == 404:
        logger.warning(f"Arquivo {file_path} não encontrado.")
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    response.raise_for_status()

    content = response.json()["content"]
    decoded_content = base64.b64decode(content).decode("utf-8")
    logger.info(f"Conteúdo do arquivo {file_path} recuperado com sucesso.")
    return decoded_content


async def fetch_branches(client: httpx.AsyncClient, owner: str, repo: str) -> List[str]:
    url = f"https://api.github.com/repos/{owner}/{repo}/branches"

    logger.info(f"Buscando branches de {url}")
    response = await make_github_request(client, url)
    response.raise_for_status()

    branches = [branch["name"] for branch in response.json()]
    logger.info(f"Total de branches encontradas: {len(branches)}")
    return branches


async def fetch_tags(client: httpx.AsyncClient, owner: str, repo: str) -> List[str]:
    url = f"https://api.github.com/repos/{owner}/{repo}/tags"

    logger.info(f"Buscando tags de {url}")
    response = await make_github_request(client, url)
    response.raise_for_status()

    tags = [tag["name"] for tag in response.json()]
    logger.info(f"Total de tags encontradas: {len(tags)}")
    return tags


async def search_repositories(
    client: httpx.AsyncClient,
    query: str,
    sort: str = "stars",
    order: str = "desc",
    per_page: int = 30,
    page: int = 1,
) -> Dict:
    url = f"https://api.github.com/search/repositories?q={query}&sort={sort}&order={order}&per_page={per_page}&page={page}"

    logger.info(f"Pesquisando repositórios com a query: {query}")
    response = await make_github_request(client, url)
    response.raise_for_status()

    data = response.json()
    repositories = [
        {
            "name": repo["full_name"],
            "description": repo["description"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
        }
        for repo in data["items"]
    ]

    logger.info(f"Total de repositórios encontrados: {data['total_count']}")
    return {
        "total_count": data["total_count"],
        "repositories": repositories,
    }


async def search_markdown_content(
    client: httpx.AsyncClient, owner: str, repo: str, query: str, ref: str = "main"
) -> List[Dict[str, str]]:
    logger.info(
        f"Pesquisando conteúdo em arquivos Markdown no repositório {owner}/{repo}. Query: {query}, Ref: {ref}"
    )

    md_files = await fetch_markdown_files(client, owner, repo, ref=ref)
    results = []

    for file in md_files:
        try:
            content = await fetch_file_content(
                client, owner, repo, file["path"], ref=ref
            )
            if query.lower() in content.lower():
                results.append(
                    {
                        "file_path": file["path"],
                        "name": file["name"],
                        "url": file["html_url"],
                        "excerpt": extract_excerpt(content, query),
                    }
                )
        except httpx.HTTPStatusError as e:
            logger.error(f"Erro ao buscar conteúdo do arquivo {file['path']}: {str(e)}")

    logger.info(f"Pesquisa concluída. Total de arquivos encontrados: {len(results)}")
    return results


def extract_excerpt(content: str, query: str, context_length: int = 100) -> str:
    index = content.lower().find(query.lower())
    if index == -1:
        return ""
    start = max(0, index - context_length)
    end = min(len(content), index + len(query) + context_length)
    excerpt = content[start:end]
    return f"...{excerpt.strip()}..."
