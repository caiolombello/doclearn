# Projeto de Integração com API do GitHub

Este projeto é uma aplicação Python que fornece uma interface para interagir com a API do GitHub, permitindo operações como listagem de arquivos Markdown, obtenção de conteúdo, e listagem de branches e tags de um repositório.

## Visão Geral

O objetivo principal do projeto é permitir que os usuários realizem operações relacionadas ao GitHub de forma simples e eficiente. A aplicação é dividida em duas partes principais: a API, que gerencia as rotas e requisições, e a lógica de negócios, que contém as funcionalidades principais do projeto.

## Estrutura do Projeto

- **`main.py`**: Ponto de entrada da aplicação.
- **`api/`**: Contém a implementação das rotas da API.
  - **`routes.py`**: Define as rotas e os manipuladores de requisições.
- **`core/`**: Contém a lógica de negócios e funcionalidades principais.
  - **`filters.py`**: Implementa filtros para processar dados.
  - **`github_client.py`**: Gerencia a comunicação com a API do GitHub.
- **`docs/`**: Contém a documentação do projeto.
  - **`introduction.md`**: Visão geral do projeto, requisitos, e instruções para execução.

## Requisitos

- Python 3.x
- [uv](https://astral.sh/uv/) para gerenciar e executar o ambiente.

## Instalação e Execução

### Passo 1: Clonar o Repositório

Clone o repositório em sua máquina local usando o comando:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Instalar e Configurar o uv

Instale o `uv` seguindo as instruções abaixo:

#### Para macOS e Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Para Windows:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Passo 3: Criar o Ambiente Virtual com uv

Crie um ambiente virtual usando o `uv`:

```bash
uv -n nome_do_projeto
```

Ative o ambiente virtual criado:

```bash
uv
```

### Passo 4: Instalar Dependências

Instale as dependências necessárias dentro do ambiente `uv`:

```bash
uv run pip install -r requirements.txt
```

### Passo 5: Executar a Aplicação

Inicie a aplicação:

```bash
uv run python main.py
```

A aplicação estará disponível em `http://localhost:8000`.

## Uso

A aplicação expõe uma série de endpoints para interagir com a API do GitHub. Veja a [documentação](src/doclearn/docs/code/introduction.md) para mais detalhes sobre como utilizar esses endpoints.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir, por favor, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.