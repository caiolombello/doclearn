---

title: Requests  
description: 'Endpoints para gerenciamento de arquivos Markdown, informações de repositório e funcionalidades de pesquisa no GitHub.'

---

# Requests

Este documento contém exemplos de comandos `curl` para interagir com os endpoints da API, facilitando o uso das rotas para gerenciar arquivos Markdown, informações do repositório e realizar pesquisas.

### 1. `GET /markdowns/`

Lista arquivos Markdown com opções de filtragem.

```bash
curl -X GET "http://localhost:8000/markdowns/?owner=your_owner&repo=your_repo&ref=main&name_query=README&min_size=100&max_size=5000&min_date=2023-01-01T00:00:00&max_date=2024-01-01T00:00:00&path_query=docs/"
```

### 2. `GET /markdowns/{file_path:path}`

Recupera o conteúdo de um arquivo Markdown específico.

```bash
curl -X GET "http://localhost:8000/markdowns/docs/some_file.md?owner=your_owner&repo=your_repo&ref=main"
```

### 3. `GET /markdowns/all/`

Recupera o conteúdo de todos os arquivos Markdown no repositório.

```bash
curl -X GET "http://localhost:8000/markdowns/all/?owner=your_owner&repo=your_repo&ref=main"
```

### 4. `GET /branches/`

Lista todas as branches do repositório.

```bash
curl -X GET "http://localhost:8000/branches/?owner=your_owner&repo=your_repo"
```

### 5. `GET /tags/`

Lista todas as tags do repositório.

```bash
curl -X GET "http://localhost:8000/tags/?owner=your_owner&repo=your_repo"
```

### 6. `GET /search/repositories`

Pesquisa repositórios no GitHub.

```bash
curl -X GET "http://localhost:8000/search/repositories?query=fastapi&sort=stars&order=desc&per_page=10&page=1"
```

### 7. `GET /search/content`

Pesquisa conteúdo em arquivos Markdown de um repositório específico.

```bash
curl -X GET "http://localhost:8000/search/content?query=fastapi&owner=your_owner&repo=your_repo&ref=main"
```

Substitua `your_owner` e `your_repo` pelos nomes apropriados do proprietário e do repositório ao fazer as requisições.

## Notas

- Todos os endpoints requerem autenticação. Certifique-se de incluir o token de acesso apropriado nos cabeçalhos da requisição.
- Os parâmetros de consulta podem ser combinados para refinar os resultados da pesquisa.
- Para endpoints que aceitam um caminho de arquivo (`file_path`), certifique-se de codificar corretamente o caminho na URL.