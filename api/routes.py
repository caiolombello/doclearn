from fastapi import APIRouter, HTTPException, Query
from doclearn.core.github_client import fetch_markdown_files, fetch_file_content, fetch_branches, fetch_tags
from doclearn.core.filters import filter_markdown_files
from datetime import datetime
import httpx
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/markdowns/")
async def list_markdown_files(
    owner: str = Query(..., description="The repository owner's username."),
    repo: str = Query(..., description="The repository name."),
    ref: str = "main",
    name_query: str = Query(None, description="Search files by name."),
    min_size: int = Query(None, description="Filter by minimum file size."),
    max_size: int = Query(None, description="Filter by maximum file size."),
    min_date: datetime = Query(None, description="Filter by minimum modification date."),
    max_date: datetime = Query(None, description="Filter by maximum modification date."),
    path_query: str = Query(None, description="Filter by file path.")
):
    logger.info(f"Listing markdown files for repository {owner}/{repo}. Ref: {ref}, Filters: {locals()}")
    try:
        async with httpx.AsyncClient() as client:
            md_files = await fetch_markdown_files(client, owner, repo, ref=ref)
        
        filtered_files = filter_markdown_files(
            md_files, name_query=name_query, min_size=min_size, max_size=max_size,
            min_date=min_date, max_date=max_date, path_query=path_query
        )
        logger.info(f"Successfully listed markdown files. Total found: {len(filtered_files)}")
        return {"markdown_files": filtered_files}
    except httpx.HTTPStatusError as e:
        logger.error(f"Error listing markdown files: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@router.get("/markdowns/{file_path:path}")
async def get_markdown_content(
    file_path: str,
    owner: str = Query(..., description="The repository owner's username."),
    repo: str = Query(..., description="The repository name."),
    ref: str = "main"
):
    logger.info(f"Fetching content of markdown file: {file_path} from repository {owner}/{repo}, Ref: {ref}")
    try:
        async with httpx.AsyncClient() as client:
            content = await fetch_file_content(client, owner, repo, file_path, ref=ref)
        logger.info(f"Successfully fetched content of file {file_path}.")
        return {"file_path": file_path, "content": content}
    except httpx.HTTPStatusError as e:
        logger.error(f"Error fetching content of file {file_path}: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@router.get("/branches/")
async def list_branches(
    owner: str = Query(..., description="The repository owner's username."),
    repo: str = Query(..., description="The repository name.")
):
    logger.info(f"Listing branches for repository {owner}/{repo}.")
    try:
        async with httpx.AsyncClient() as client:
            branches = await fetch_branches(client, owner, repo)
        logger.info(f"Successfully listed branches. Total found: {len(branches)}")
        return {"branches": branches}
    except httpx.HTTPStatusError as e:
        logger.error(f"Error listing branches: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@router.get("/tags/")
async def list_tags(
    owner: str = Query(..., description="The repository owner's username."),
    repo: str = Query(..., description="The repository name.")
):
    logger.info(f"Listing tags for repository {owner}/{repo}.")
    try:
        async with httpx.AsyncClient() as client:
            tags = await fetch_tags(client, owner, repo)
        logger.info(f"Successfully listed tags. Total found: {len(tags)}")
        return {"tags": tags}
    except httpx.HTTPStatusError as e:
        logger.error(f"Error listing tags: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
