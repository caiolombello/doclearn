---

title: Requests  
description: 'Endpoints for managing Markdown files, repository information, and GitHub search functionalities.'

---

# Requests

This document contains examples of `curl` commands to interact with the API endpoints, facilitating the use of routes for managing Markdown files, repository information, and performing searches.

### 1. `GET /markdowns/`

Lists Markdown files with filtering options.

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&name_query=README&min_size=100&max_size=5000&min_date=2023-01-01T00:00:00&max_date=2024-01-01T00:00:00&path_query=docs/"
```

### 2. `GET /markdowns/{file_path:path}`

Retrieves the content of a specific Markdown file.

```bash
curl -X GET "http://localhost:8000/markdowns/docs/some_file.md?owner=your_owner&repo=your_repo&ref=main"
```

### 3. `GET /markdowns/all/`

Retrieves the content of all Markdown files in the repository.

```bash
curl -X GET "http://localhost:8000/markdowns/all/?owner=your_owner&repo=your_repo&ref=main"
```

### 4. `GET /branches/`

Lists all branches of the repository.

```bash
curl -X GET "http://localhost:8000/branches/?owner=your_owner&repo=your_repo"
```

### 5. `GET /tags/`

Lists all tags of the repository.

```bash
curl -X GET "http://localhost:8000/tags/?owner=your_owner&repo=your_repo"
```

### 6. `GET /search/repositories`

Searches for repositories on GitHub.

```bash
curl -X GET "http://localhost:8000/search/repositories?query=fastapi&sort=stars&order=desc&per_page=10&page=1"
```

### 7. `GET /search/content`

Searches for content in Markdown files of a specific repository.

```bash
curl -X GET "http://localhost:8000/search/content?query=fastapi&owner=your_owner&repo=your_repo&ref=main"
```

Replace `your_owner` and `your_repo` with the appropriate owner and repository names when making requests.

## Notes

- All endpoints require authentication. Make sure to include the appropriate access token in the request headers.
- Query parameters can be combined to refine search results.
- For endpoints that accept a file path (`file_path`), ensure that the path is correctly encoded in the URL.