from fastapi import APIRouter, HTTPException, Query, Depends
from doclearn.core.github_client import (
    fetch_markdown_files,
    fetch_file_content,
    fetch_branches,
    fetch_tags,
    search_repositories,
    get_github_client,
    search_markdown_content,
)
from doclearn.core.filters import filter_markdown_files
from datetime import datetime
import httpx
import logging
from typing import Optional

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/markdowns/")
async def list_markdown_files(
    owner: str = Query(
        ..., description="Nome de usuário do proprietário do repositório."
    ),
    repo: str = Query(..., description="Nome do repositório."),
    ref: str = Query("main", description="Referência (branch, tag ou commit)."),
    name_query: Optional[str] = Query(None, description="Pesquisar arquivos por nome."),
    min_size: Optional[int] = Query(
        None, description="Filtrar por tamanho mínimo do arquivo."
    ),
    max_size: Optional[int] = Query(
        None, description="Filtrar por tamanho máximo do arquivo."
    ),
    min_date: Optional[datetime] = Query(
        None, description="Filtrar por data mínima de modificação."
    ),
    max_date: Optional[datetime] = Query(
        None, description="Filtrar por data máxima de modificação."
    ),
    path_query: Optional[str] = Query(
        None, description="Filtrar por caminho do arquivo."
    ),
    client: httpx.AsyncClient = Depends(get_github_client),
):
    logger.info(
        f"Listando arquivos markdown para o repositório {owner}/{repo}. Ref: {ref}, Filtros: {locals()}"
    )
    try:
        md_files = await fetch_markdown_files(client, owner, repo, ref=ref)
        filtered_files = filter_markdown_files(
            md_files,
            name_query=name_query,
            min_size=min_size,
            max_size=max_size,
            min_date=min_date,
            max_date=max_date,
            path_query=path_query,
        )
        logger.info(
            f"Arquivos markdown listados com sucesso. Total encontrado: {len(filtered_files)}"
        )
        return {"markdown_files": filtered_files}
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao listar arquivos markdown: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.get("/markdowns/{file_path:path}")
async def get_markdown_content(
    file_path: str,
    owner: str = Query(
        ..., description="Nome de usuário do proprietário do repositório."
    ),
    repo: str = Query(..., description="Nome do repositório."),
    ref: str = Query("main", description="Referência (branch, tag ou commit)."),
    client: httpx.AsyncClient = Depends(get_github_client),
):
    logger.info(
        f"Buscando conteúdo do arquivo markdown: {file_path} do repositório {owner}/{repo}, Ref: {ref}"
    )
    try:
        content = await fetch_file_content(client, owner, repo, file_path, ref=ref)
        logger.info(f"Conteúdo do arquivo {file_path} obtido com sucesso.")
        return {"file_path": file_path, "content": content}
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao buscar conteúdo do arquivo {file_path}: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.get("/branches/")
async def list_branches(
    owner: str = Query(
        ..., description="Nome de usuário do proprietário do repositório."
    ),
    repo: str = Query(..., description="Nome do repositório."),
    client: httpx.AsyncClient = Depends(get_github_client),
):
    logger.info(f"Listando branches para o repositório {owner}/{repo}.")
    try:
        branches = await fetch_branches(client, owner, repo)
        logger.info(f"Branches listadas com sucesso. Total encontrado: {len(branches)}")
        return {"branches": branches}
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao listar branches: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.get("/tags/")
async def list_tags(
    owner: str = Query(
        ..., description="Nome de usuário do proprietário do repositório."
    ),
    repo: str = Query(..., description="Nome do repositório."),
    client: httpx.AsyncClient = Depends(get_github_client),
):
    logger.info(f"Listando tags para o repositório {owner}/{repo}.")
    try:
        tags = await fetch_tags(client, owner, repo)
        logger.info(f"Tags listadas com sucesso. Total encontrado: {len(tags)}")
        return {"tags": tags}
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao listar tags: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.get("/search/repositories")
async def search_github_repositories(
    query: str = Query(..., description="Termo de pesquisa para repositórios"),
    sort: str = Query(
        "stars",
        description="Campo para ordenação (stars, forks, help-wanted-issues, updated)",
    ),
    order: str = Query("desc", description="Ordem de classificação (asc ou desc)"),
    per_page: int = Query(30, description="Número de resultados por página"),
    page: int = Query(1, description="Número da página"),
    client: httpx.AsyncClient = Depends(get_github_client),
):
    try:
        result = await search_repositories(client, query, sort, order, per_page, page)
        logger.info(
            f"Pesquisa de repositórios concluída. Total encontrado: {result['total_count']}"
        )
        return result
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao pesquisar repositórios: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.get("/search/content")
async def search_markdown_content_route(
    query: str = Query(..., description="Termo de pesquisa no conteúdo dos arquivos"),
    owner: str = Query(..., description="Nome do proprietário do repositório"),
    repo: str = Query(..., description="Nome do repositório"),
    ref: str = Query("main", description="Referência (branch, tag ou commit)"),
    client: httpx.AsyncClient = Depends(get_github_client),
):
    try:
        results = await search_markdown_content(client, owner, repo, query, ref)
        logger.info(
            f"Pesquisa de conteúdo concluída. Total de resultados: {len(results)}"
        )
        return {"results": results}
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao pesquisar conteúdo: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
