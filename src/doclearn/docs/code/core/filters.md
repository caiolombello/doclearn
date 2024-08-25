---
title: Filters
description: 'Functions for filtering Markdown files based on specific criteria.'
---

# filters.py

This module contains the `filter_markdown_files` function, which allows filtering a list of Markdown files based on criteria such as name, size, modification date, and path.

## Function: filter_markdown_files

```python
def filter_markdown_files(md_files, name_query=None, min_size=None, max_size=None, min_date=None, max_date=None, path_query=None):
```


### Parameters

- `md_files` (list): A list of dictionaries representing Markdown files. Each dictionary should contain the keys `name`, `size`, and `last_modified`.
- `name_query` (str, optional): A string to filter files by name. Only files whose name contains this string (case-insensitive) will be included.
- `min_size` (int, optional): The minimum file size in bytes. Only files larger than or equal to this size will be included.
- `max_size` (int, optional): The maximum file size in bytes. Only files smaller than or equal to this size will be included.
- `min_date` (datetime, optional): The minimum modification date. Only files modified after this date will be included.
- `max_date` (datetime, optional): The maximum modification date. Only files modified before this date will be included.
- `path_query` (str, optional): A string to filter files by path. Only files whose path contains this string (case-insensitive) will be included.

### Return

- (list): A list of files that meet the specified filtering criteria.

### Usage Example

```python
from datetime import datetime

md_files = [
    {"name": "example1.md", "size": 1500, "last_modified": "2023-10-01T12:00:00Z", "path": "docs/example1.md"},
    {"name": "example2.md", "size": 2500, "last_modified": "2023-09-15T12:00:00Z", "path": "docs/example2.md"},
]

filtered = filter_markdown_files(md_files, name_query="example", min_size=1000, min_date=datetime(2023, 9, 1))
```


In this example, the `filter_markdown_files` function will return all files that contain "example" in the name, have a size greater than or equal to 1000 bytes, and were modified after September 1, 2023.