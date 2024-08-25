# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.1.0] - 2024-08-24

### Adicionado

- ✨ feat(core/github_client): Implementada rotação de tokens para requisições à API do GitHub para lidar com limites de taxa.

### Corrigido

- ⬇️ fix(dependencies): Downgrade do `cz_conventional_commits` da versão 1.2.0 para 1.1.0.
- 🔖 fix(version): Downgrade da versão de 1.2.0 para 1.1.0 no `pyproject.toml`.

## [1.0.0] - 2024-08-22

### Adicionado

- 🎉 feat(initial-setup): Inicializado o projeto com estrutura básica, incluindo rotas de API, lógica principal e documentação.
- ✨ feat(api): Adicionadas rotas iniciais da API para gerenciar arquivos Markdown e informações do repositório.
- ✨ feat(docker): Adicionado Dockerfile e atualizadas dependências para uvicorn.
- ✨ feat(docs): Adicionadas instruções de uso do Docker e link de integração GPT ao README.

[1.1.0]: https://github.com/caiolombello/doclearn/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/caiolombello/doclearn/releases/tag/v1.0.0