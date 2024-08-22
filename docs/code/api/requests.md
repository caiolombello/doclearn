# Requests

This document contains examples of `curl` commands to interact with the API endpoints, facilitating the use of routes for managing Markdown files and repository information.

### 1. `GET /markdowns/`

List Markdown files with filtering options.

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&name_query=README&min_size=100&max_size=5000&min_date=2023-01-01T00:00:00&max_date=2024-01-01T00:00:00&path_query=docs/"
```

Let's break this `curl` command into several smaller commands, demonstrating different possibilities of using the parameters:

#### 1.1. List Markdown files with reference filter (`ref`)

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main"
```

This command lists all Markdown files in the `main` branch.

#### 1.2. Filter files by name (`name_query`)

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&name_query=README"
```

This command filters the Markdown files whose name contains "README".

#### 1.3. Filter files by minimum and maximum size (`min_size` and `max_size`)

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&min_size=100&max_size=5000"
```

This command returns Markdown files that are between 100 bytes and 5000 bytes in size.

#### 1.4. Filter files by modification date (`min_date` and `max_date`)

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&min_date=2023-01-01T00:00:00&max_date=2024-01-01T00:00:00"
```

This command filters the Markdown files modified between January 1, 2023, and January 1, 2024.

#### 1.5. Filter files by specific path (`path_query`)

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&path_query=docs/"
```

This command lists Markdown files that are inside the `docs/` directory in the repository.

#### 1.6. Combining multiple filters

You can combine these parameters to further refine your search:

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&name_query=README&min_size=100&max_size=5000&min_date=2023-01-01T00:00:00&max_date=2024-01-01T00:00:00&path_query=docs/"
```

This command returns Markdown files inside the `docs/` directory, whose name contains "README", with a size between 100 and 5000 bytes, modified between the specified dates, in the `main` branch.

### 2. `GET /markdowns/{file_path:path}`

Retrieve the content of a specific Markdown file.

```bash
curl -X GET "http://localhost:8000/markdowns/docs/some_file.md?owner=your_owner&repo=your_repo&ref=main"
```

### 3. `GET /markdowns/all/`

Retrieve the content of all Markdown files in the repository.

```bash
curl -X GET "http://localhost:8000/markdowns/all/?owner=your_owner&repo=your_repo&ref=main"
```

### 4. `GET /branches/`

List all branches in the repository.

```bash
curl -X GET "http://localhost:8000/branches/?owner=your_owner&repo=your_repo"
```

### 5. `GET /tags/`

List all tags in the repository.

```bash
curl -X GET "http://localhost:8000/tags/?owner=your_owner&repo=your_repo"
```

Replace `your_owner` and `your_repo` with the appropriate owner and repository names when making the requests.