import logging
from typing import Dict, List

import httpx
from fastapi import HTTPException

from doclearn.config import Config

logger = logging.getLogger(__name__)


async def search_google(
    client: httpx.AsyncClient, query: str, num_results: int = 10
) -> List[Dict[str, str]]:
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": Config.google_api_key,
        "cx": Config.google_search_engine_id,
        "q": query,
        "num": num_results,
    }

    logger.info(f"Performing Google search for: {query}")
    try:
        response = await client.get(url, params=params)
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error during Google search: {str(e)}")
        raise HTTPException(
            status_code=e.response.status_code, detail="Error during Google search"
        )

    data = response.json()
    results = [
        {"title": item["title"], "link": item["link"], "snippet": item["snippet"]}
        for item in data.get("items", [])
    ]

    logger.info(f"Google search completed. Total results: {len(results)}")
    return results
