import base64
import logging
from itertools import cycle
from fastapi import HTTPException
from doclearn.config import Config

logger = logging.getLogger(__name__)

token_cycle = cycle(Config.tokens)

def get_next_token():
    return next(token_cycle)

async def make_github_request(client, url):
    for _ in range(len(Config.tokens)):
        token = get_next_token()
        headers = {"Authorization": f"token {token}"} if token else {}
        
        response = await client.get(url, headers=headers)
        if response.status_code != 403:  # Não é um erro de limite de taxa
            return response
        
        logger.warning(f"Rate limit atingido para o token atual. Alternando para o próximo token.")
    
    raise HTTPException(status_code=429, detail="Limite de taxa excedido para todos os tokens")

async def fetch_markdown_files(client, owner, repo, path="", ref="main"):
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

async def fetch_file_content(client, owner, repo, file_path, ref="main"):
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

async def fetch_branches(client, owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/branches"

    logger.info(f"Buscando branches de {url}")
    response = await make_github_request(client, url)
    response.raise_for_status()

    branches = [branch["name"] for branch in response.json()]
    logger.info(f"Total de branches encontradas: {len(branches)}")
    return branches

async def fetch_tags(client, owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/tags"

    logger.info(f"Buscando tags de {url}")
    response = await make_github_request(client, url)
    response.raise_for_status()

    tags = [tag["name"] for tag in response.json()]
    logger.info(f"Total de tags encontradas: {len(tags)}")
    return tags