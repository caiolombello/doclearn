---
title: github_client
description: 'Cliente assíncrono para interagir com a API do GitHub, permitindo a busca de arquivos Markdown, conteúdo de arquivos, branches, tags e pesquisa de repositórios.'
---

# github_client

Este módulo fornece funções assíncronas para interagir com a API do GitHub, permitindo a busca de arquivos Markdown, conteúdo de arquivos, branches, tags e pesquisa de repositórios.

## Configurações e Utilitários

- `token_cycle`: Um ciclo de tokens de acesso do GitHub para lidar com limites de taxa.
- `get_next_token()`: Retorna o próximo token disponível do ciclo.
- `get_github_client()`: Cria e retorna um cliente HTTP assíncrono.

## Funções de Requisição

### `make_github_request(client, url)`

Realiza uma requisição à API do GitHub, alternando tokens em caso de limite de taxa.

#### Parâmetros

- `client`: Instância do cliente HTTP assíncrono.
- `url`: URL da requisição.

#### Retorno

Retorna a resposta da requisição ou lança uma exceção em caso de erro.

## Funções de Busca de Arquivos e Conteúdo

### `fetch_markdown_files(client, owner, repo, path="", ref="main")`

Busca arquivos Markdown em um repositório GitHub.

#### Parâmetros

- `client`: Instância do cliente HTTP assíncrono.
- `owner`: Proprietário do repositório.
- `repo`: Nome do repositório.
- `path`: Caminho do diretório a ser pesquisado (padrão é "").
- `ref`: A referência do branch (padrão é "main").

#### Retorno

Retorna uma lista de arquivos Markdown encontrados.

### `fetch_file_content(client, owner, repo, file_path, ref="main")`

Busca o conteúdo de um arquivo específico no repositório.

#### Parâmetros

- `client`: Instância do cliente HTTP assíncrono.
- `owner`: Proprietário do repositório.
- `repo`: Nome do repositório.
- `file_path`: Caminho do arquivo a ser buscado.
- `ref`: A referência do branch (padrão é "main").

#### Retorno

Retorna o conteúdo do arquivo decodificado em formato de string.

#### Exceções

- Lança `HTTPException` com status 404 se o arquivo não for encontrado.

## Funções de Busca de Informações do Repositório

### `fetch_branches(client, owner, repo)`

Busca todos os branches do repositório.

#### Parâmetros

- `client`: Instância do cliente HTTP assíncrono.
- `owner`: Proprietário do repositório.
- `repo`: Nome do repositório.

#### Retorno

Retorna uma lista com os nomes dos branches.

### `fetch_tags(client, owner, repo)`

Busca todas as tags do repositório.

#### Parâmetros

- `client`: Instância do cliente HTTP assíncrono.
- `owner`: Proprietário do repositório.
- `repo`: Nome do repositório.

#### Retorno

Retorna uma lista com os nomes das tags.

## Funções de Pesquisa

### `search_repositories(client, query, sort="stars", order="desc", per_page=30, page=1)`

Pesquisa repositórios no GitHub com base em uma query.

#### Parâmetros

- `client`: Instância do cliente HTTP assíncrono.
- `query`: Termo de pesquisa.
- `sort`: Campo para ordenação (padrão é "stars").
- `order`: Ordem de classificação (padrão é "desc").
- `per_page`: Número de resultados por página (padrão é 30).
- `page`: Número da página (padrão é 1).

#### Retorno

Retorna um dicionário com o total de resultados e uma lista de repositórios encontrados.

### `search_markdown_content(client, owner, repo, query, ref="main")`

Pesquisa conteúdo em arquivos Markdown de um repositório específico.

#### Parâmetros

- `client`: Instância do cliente HTTP assíncrono.
- `owner`: Proprietário do repositório.
- `repo`: Nome do repositório.
- `query`: Termo de pesquisa.
- `ref`: A referência do branch (padrão é "main").

#### Retorno

Retorna uma lista de dicionários contendo informações sobre os arquivos Markdown que contêm a query.

### `extract_excerpt(content, query, context_length=100)`

Extrai um trecho do conteúdo ao redor da ocorrência da query.

#### Parâmetros

- `content`: Conteúdo do arquivo.
- `query`: Termo de pesquisa.
- `context_length`: Número de caracteres de contexto (padrão é 100).

#### Retorno

Retorna um trecho do conteúdo com a query destacada.