---
title: filters
description: 'Funções para filtrar arquivos Markdown com base em critérios específicos.'
---

# filters.py

Este módulo contém a função `filter_markdown_files`, que permite filtrar uma lista de arquivos Markdown com base em critérios como nome, tamanho, data de modificação e caminho.

## Função: filter_markdown_files

```python
def filter_markdown_files(md_files, name_query=None, min_size=None, max_size=None, min_date=None, max_date=None, path_query=None):
```

### Parâmetros

- `md_files` (list): Uma lista de dicionários representando arquivos Markdown. Cada dicionário deve conter as chaves `name`, `size` e `last_modified`.
- `name_query` (str, opcional): Uma string para filtrar arquivos pelo nome. Apenas arquivos cujo nome contém essa string (ignorando maiúsculas/minúsculas) serão incluídos.
- `min_size` (int, opcional): O tamanho mínimo do arquivo em bytes. Apenas arquivos maiores ou iguais a esse tamanho serão incluídos.
- `max_size` (int, opcional): O tamanho máximo do arquivo em bytes. Apenas arquivos menores ou iguais a esse tamanho serão incluídos.
- `min_date` (datetime, opcional): A data mínima de modificação. Apenas arquivos modificados após essa data serão incluídos.
- `max_date` (datetime, opcional): A data máxima de modificação. Apenas arquivos modificados antes dessa data serão incluídos.
- `path_query` (str, opcional): Uma string para filtrar arquivos pelo caminho. Apenas arquivos cujo caminho contém essa string (ignorando maiúsculas/minúsculas) serão incluídos.

### Retorno

- (list): Uma lista de arquivos que atendem aos critérios de filtragem especificados.

### Exemplo de Uso

```python
from datetime import datetime

md_files = [
    {"name": "example1.md", "size": 1500, "last_modified": "2023-10-01T12:00:00Z", "path": "docs/example1.md"},
    {"name": "example2.md", "size": 2500, "last_modified": "2023-09-15T12:00:00Z", "path": "docs/example2.md"},
]

filtered = filter_markdown_files(md_files, name_query="example", min_size=1000, min_date=datetime(2023, 9, 1))
```

Neste exemplo, a função `filter_markdown_files` retornará todos os arquivos que contêm "example" no nome, têm um tamanho maior ou igual a 1000 bytes e foram modificados após 1º de setembro de 2023.