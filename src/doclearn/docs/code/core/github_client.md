---
title: github_client
description: 'Asynchronous client for interacting with the GitHub API, allowing the retrieval of Markdown files, file content, branches, tags, and repository search.'
---

# github_client

This module provides asynchronous functions to interact with the GitHub API, allowing the retrieval of Markdown files, file content, branches, tags, and repository search.

## Configuration and Utilities

- `token_cycle`: A cycle of GitHub access tokens to handle rate limits.
- `get_next_token()`: Returns the next available token from the cycle.
- `get_github_client()`: Creates and returns an asynchronous HTTP client.

## Request Functions

### `make_github_request(client, url)`

Makes a request to the GitHub API, alternating tokens in case of rate limit.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `url`: Request URL.

#### Return

Returns the request response or raises an exception in case of error.

## File and Content Retrieval Functions

### `fetch_markdown_files(client, owner, repo, path="", ref="main")`

Retrieves Markdown files from a GitHub repository.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `owner`: Repository owner.
- `repo`: Repository name.
- `path`: Directory path to search (default is "").
- `ref`: Branch reference (default is "main").

#### Return

Returns a list of found Markdown files.

### `fetch_file_content(client, owner, repo, file_path, ref="main")`

Retrieves the content of a specific file in the repository.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `owner`: Repository owner.
- `repo`: Repository name.
- `file_path`: Path of the file to be retrieved.
- `ref`: Branch reference (default is "main").

#### Return

Returns the file content decoded as a string.

#### Exceptions

- Raises `HTTPException` with status 404 if the file is not found.

## Repository Information Retrieval Functions

### `fetch_branches(client, owner, repo)`

Retrieves all branches of the repository.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `owner`: Repository owner.
- `repo`: Repository name.

#### Return

Returns a list with the names of the branches.

### `fetch_tags(client, owner, repo)`

Retrieves all tags of the repository.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `owner`: Repository owner.
- `repo`: Repository name.

#### Return

Returns a list with the names of the tags.

## Search Functions

### `search_repositories(client, query, sort="stars", order="desc", per_page=30, page=1)`

Searches for repositories on GitHub based on a query.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `query`: Search term.
- `sort`: Field for sorting (default is "stars").
- `order`: Sort order (default is "desc").
- `per_page`: Number of results per page (default is 30).
- `page`: Page number (default is 1).

#### Return

Returns a dictionary with the total count of results and a list of found repositories.

### `search_markdown_content(client, owner, repo, query, ref="main")`

Searches for content in Markdown files of a specific repository.

#### Parameters

- `client`: Instance of the asynchronous HTTP client.
- `owner`: Repository owner.
- `repo`: Repository name.
- `query`: Search term.
- `ref`: Branch reference (default is "main").

#### Return

Returns a list of dictionaries containing information about Markdown files that contain the query.

### `extract_excerpt(content, query, context_length=100)`

Extracts an excerpt of the content around the query occurrence.

#### Parameters

- `content`: File content.
- `query`: Search term.
- `context_length`: Number of context characters (default is 100).

#### Return

Returns an excerpt of the content with the query highlighted.