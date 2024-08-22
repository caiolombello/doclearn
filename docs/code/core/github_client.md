---
title: github_client
description: 'Cliente assíncrono para interagir com a API do GitHub, permitindo a busca de arquivos Markdown, conteúdo de arquivos, branches e tags de um repositório.'
---

# github_client

Este módulo fornece funções assíncronas para interagir com a API do GitHub, permitindo a busca de arquivos Markdown, conteúdo de arquivos, branches e tags de um repositório específico.

## Configurações

As seguintes variáveis são utilizadas para configurar o acesso ao repositório:

- `owner`: O proprietário do repositório (ex: "aws").
- `repo`: O nome do repositório (ex: "karpenter-provider-aws").
- `token`: Um token de acesso pessoal do GitHub. Este é opcional se o repositório for público.

## Funções

### `fetch_markdown_files(client, path="", ref="main")`

Busca arquivos Markdown em um repositório GitHub.

#### Parâmetros

- `client`: Instância do cliente HTTP (ex: httpx).
- `path`: Caminho do diretório a ser pesquisado (padrão é "").
- `ref`: A referência do branch (padrão é "main").

#### Retorno

Retorna uma lista de arquivos Markdown encontrados.

### `fetch_file_content(client, file_path, ref="main")`

Busca o conteúdo de um arquivo específico no repositório.

#### Parâmetros

- `client`: Instância do cliente HTTP (ex: httpx).
- `file_path`: Caminho do arquivo a ser buscado.
- `ref`: A referência do branch (padrão é "main").

#### Retorno

Retorna o conteúdo do arquivo decodificado em formato de string.

#### Exceções

- Lança `HTTPException` com status 404 se o arquivo não for encontrado.

### `fetch_branches(client)`

Busca todos os branches do repositório.

#### Parâmetros

- `client`: Instância do cliente HTTP (ex: httpx).

#### Retorno

Retorna uma lista com os nomes dos branches.

### `fetch_tags(client)`

Busca todas as tags do repositório.

#### Parâmetros

- `client`: Instância do cliente HTTP (ex: httpx).

#### Retorno

Retorna uma lista com os nomes das tags.