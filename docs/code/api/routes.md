---

title: routes  
description: 'Endpoints for handling Markdown files and repository information.'

---

# routes.py

This module defines the API routes for managing Markdown files and repository-related information. It uses the FastAPI framework to create asynchronous endpoints.

## Endpoints

### `GET /markdowns/`

List Markdown files with filtering options.

#### Query Parameters

- `owner` (str): Repository owner name.
- `repo` (str): Repository name.
- `ref` (str, optional): Repository reference (default: "main").
- `name_query` (str, optional): Search files by name.
- `min_size` (int, optional): Filter by minimum file size.
- `max_size` (int, optional): Filter by maximum file size.
- `min_date` (datetime, optional): Filter by minimum modification date.
- `max_date` (datetime, optional): Filter by maximum modification date.
- `path_query` (str, optional): Filter by file path.

#### Response

Returns a JSON with the list of filtered Markdown files.

#### Exceptions

- `HTTPException`: Raised in case of an HTTP request error.

---

### `GET /markdowns/{file_path:path}`

Retrieve the content of a specific Markdown file.

#### Parameters

- `owner` (str): Repository owner name.
- `repo` (str): Repository name.
- `file_path` (str): Path to the Markdown file.
- `ref` (str, optional): Repository reference (default: "main").

#### Response

Returns a JSON with the file path and its content.

#### Exceptions

- `HTTPException`: Raised in case of an HTTP request error.

---

### `GET /markdowns/all/`

Retrieve the content of all Markdown files in the repository.

#### Query Parameters

- `owner` (str): Repository owner name.
- `repo` (str): Repository name.
- `ref` (str, optional): Repository reference (default: "main").

#### Response

Returns a JSON with the content of all Markdown files.

#### Exceptions

- `HTTPException`: Raised in case of an HTTP request error.

---

### `GET /branches/`

List all branches in the repository.

#### Query Parameters

- `owner` (str): Repository owner name.
- `repo` (str): Repository name.

#### Response

Returns a JSON with the list of branches.

#### Exceptions

- `HTTPException`: Raised in case of an HTTP request error.

---

### `GET /tags/`

List all tags in the repository.

#### Query Parameters

- `owner` (str): Repository owner name.
- `repo` (str): Repository name.

#### Response

Returns a JSON with the list of tags.

#### Exceptions

- `HTTPException`: Raised in case of an HTTP request error.