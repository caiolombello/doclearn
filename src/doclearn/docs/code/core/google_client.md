---
title: google_client
description: 'Module for interacting with the Google Custom Search API.'
---

# google_client

This module provides functionality to interact with the Google Custom Search API, allowing for programmatic Google searches.

## Functions

### `search_google(client, query, num_results=10)`

Performs a Google search using the Custom Search API.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `query`: Search term for Google.
- `num_results`: Number of results to be returned (default is 10).

#### Return

Returns a list of dictionaries containing search results, each with 'title', 'link', and 'snippet' keys.

#### Exceptions

- Raises `HTTPException` if there's an error during the API request.