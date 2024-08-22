# Use uma imagem oficial do Python como base
FROM python:3.11-slim-bullseye

# Instale dependências do sistema necessárias para o uv
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Baixe e instale o uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Configure o PATH para incluir o uv
ENV PATH="/root/.cargo/bin/:$PATH"

# Crie o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho no contêiner
COPY . /app

# Sincronize o ambiente de desenvolvimento com o uv
RUN uv sync

# Configure o ambiente virtual
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Comando para rodar a aplicação
CMD ["uv", "run", "uvicorn", "src.doclearn.main:app", "--host", "0.0.0.0", "--port", "80"]