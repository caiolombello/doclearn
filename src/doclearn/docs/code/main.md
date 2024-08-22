---
title: main.py
description: 'Arquivo principal que inicializa a aplicação FastAPI e inclui as rotas definidas.'
---

# main.py

O arquivo `main.py` é o ponto de entrada da aplicação, responsável por inicializar o servidor FastAPI e incluir as rotas definidas em outros módulos.

## Estrutura do Código

```python
from fastapi import FastAPI
from doclearn.api.routes import router

app = FastAPI()

# Inclui as rotas definidas no módulo routes
app.include_router(router)
```

### Importações

- `FastAPI`: Classe principal que cria a aplicação.
- `router`: Objeto que contém as rotas definidas, importado do módulo `routes`.

### Inicialização da Aplicação

- `app = FastAPI()`: Cria uma instância da aplicação FastAPI.

### Inclusão de Rotas

- `app.include_router(router)`: Adiciona as rotas definidas no módulo `routes` à aplicação. Isso permite que a aplicação responda a requisições HTTP nas rotas especificadas.

## Considerações

Este arquivo é essencial para o funcionamento da aplicação, pois configura o servidor e as rotas que serão utilizadas. Certifique-se de que as rotas no módulo `routes` estejam corretamente definidas para garantir o funcionamento adequado da API.