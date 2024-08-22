---
title: core
description: 'Diretório principal que contém a lógica central do projeto, incluindo filtros e integração com o GitHub.'
---

# core

O diretório `core` é responsável por abrigar a lógica central do projeto. Ele contém módulos que implementam funcionalidades essenciais, como filtros de dados e a comunicação com a API do GitHub.

## Estrutura do Diretório

- **filters.py**: Este módulo contém funções e classes que aplicam filtros a dados, permitindo a manipulação e a extração de informações relevantes.
  
- **github_client.py**: Este módulo é responsável pela integração com a API do GitHub, facilitando operações como autenticação, requisições de dados e manipulação de repositórios.

## Considerações

A organização do diretório `core` é fundamental para a manutenção e escalabilidade do projeto. Cada módulo deve ser projetado para ser reutilizável e testável, garantindo que a lógica central permaneça clara e eficiente.