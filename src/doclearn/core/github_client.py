import base64
import logging
from fastapi import HTTPException
from doclearn.config import Config

logger = logging.getLogger(__name__)


async def fetch_markdown_files(client, owner, repo, path="", ref="main"):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={ref}"
    headers = {"Authorization": f"token {Config.token}"} if Config.token else {}

    logger.info(f"Fetching markdown files from {url}")
    response = await client.get(url, headers=headers)
    response.raise_for_status()

    files = response.json()
    md_files = []

    for file in files:
        if file["type"] == "dir":
            logger.info(f"Entering directory: {file['path']}")
            md_files.extend(
                await fetch_markdown_files(client, owner, repo, file["path"], ref)
            )
        elif file["name"].endswith(".md"):
            md_files.append(file)

    logger.info(f"Total markdown files found: {len(md_files)}")
    return md_files


async def fetch_file_content(client, owner, repo, file_path, ref="main"):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={ref}"
    headers = {"Authorization": f"token {Config.token}"} if Config.token else {}

    logger.info(f"Fetching content of the file {file_path}")
    response = await client.get(url, headers=headers)
    if response.status_code == 404:
        logger.warning(f"File {file_path} not found.")
        raise HTTPException(status_code=404, detail="File not found")

    response.raise_for_status()

    content = response.json()["content"]
    decoded_content = base64.b64decode(content).decode("utf-8")
    logger.info(f"Successfully retrieved content of the file {file_path}.")
    return decoded_content


async def fetch_branches(client, owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/branches"
    headers = {"Authorization": f"token {Config.token}"} if Config.token else {}

    logger.info(f"Fetching branches from {url}")
    response = await client.get(url, headers=headers)
    response.raise_for_status()

    branches = [branch["name"] for branch in response.json()]
    logger.info(f"Total branches found: {len(branches)}")
    return branches


async def fetch_tags(client, owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/tags"
    headers = {"Authorization": f"token {Config.token}"} if Config.token else {}

    logger.info(f"Fetching tags from {url}")
    response = await client.get(url, headers=headers)
    response.raise_for_status()

    tags = [tag["name"] for tag in response.json()]
    logger.info(f"Total tags found: {len(tags)}")
    return tags
