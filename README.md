# GitDoc AI

GitDoc AI is a Python application that provides an interface for interacting with the GitHub API. It allows users to perform various operations related to GitHub repositories, such as retrieving Markdown files, listing branches and tags, and fetching the contents of specific files.

## Overview

The project is organized into two main components: the API and the business logic. The API manages routes and requests, while the core logic is implemented within the project's core modules. The primary goal is to enable users to interact with GitHub repositories in a simple and efficient way.

## Features

- List Markdown files in a repository with various filtering options.
- Retrieve the content of a specific Markdown file.
- Fetch the content of all Markdown files in a repository.
- List all branches and tags in a repository.

## Project Structure

- `main.py`: The entry point of the application, where execution begins.
- `api/`: Contains the implementation of API routes.
  - `routes.py`: Defines the routes and request handlers.
- `core/`: Contains the core business logic and functionalities.
  - `filters.py`: Implements filters to process data.
  - `github_client.py`: Manages communication with the GitHub API.
  - `google_client.py`: Manages communication with the Google Custom Search API.
- `config/`: Configuration files and settings.

## Requirements

To run this project, you will need `uv` installed on your machine. `uv` provides a comprehensive environment for managing Python versions, dependencies, and running your Python projects.

## How to Run the Project

1. **Install `uv`**: If you haven't already installed `uv`, you can do so using one of the following methods:
   - macOS and Linux:
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   - Windows:
     ```powershell
     powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```

2. **Clone the repository to your local machine**:
   ```bash
   git clone https://github.com/yourusername/gitdoc-ai.git
   ```

3. **Navigate to the project directory**:
   ```bash
   cd gitdoc-ai
   ```

4. **Create a new Python project environment using `uv`**:
   ```bash
   uv init
   ```

5. **Add dependencies to the project**:
   ```bash
   uv add fastapi httpx
   ```

6. **Sync the project's dependencies**:
   ```bash
   uv sync
   ```

7. **Run the project**:
   ```bash
   uv run main.py
   ```

## Docker Usage

To containerize the GitDoc AI application, you can use the provided Dockerfile. Below are the steps to build and run the Docker container:

1. **Build the Docker Image**:
   ```bash
   docker build -t doclearn-app .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -d -p 8000:80 doclearn-app
   ```

   This command will start the application inside a Docker container and bind the container's port 80 to your machine's port 8000.

3. **Access the Application**:
   Once the container is running, you can access the API by navigating to `http://localhost:8000` in your web browser or using tools like `curl` or Postman.

## Usage

### API Endpoints

- **GET `/markdowns/`**: Lista arquivos Markdown em um repositório com opções de filtragem.
- **GET `/markdowns/{file_path:path}`**: Recupera o conteúdo de um arquivo Markdown específico.
- **GET `/markdowns/all/`**: Busca o conteúdo de todos os arquivos Markdown em um repositório.
- **GET `/branches/`**: Lista todas as branches em um repositório.
- **GET `/tags/`**: Lista todas as tags em um repositório.
- **GET `/search/repositories`**: Pesquisa repositórios no GitHub.
- **GET `/search/content`**: Pesquisa conteúdo em arquivos Markdown de um repositório específico.
- **GET `/search/google`**: Realiza uma pesquisa no Google.

## Configuration

The application uses a configuration file located in the `config/` directory. Ensure that your GitHub token and other necessary settings are correctly configured.

## Logging

The application uses Python's built-in logging module to provide detailed logs for API calls and internal operations. Logs can be found in the configured log file or console output.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss any improvements or suggestions.

## Contact

For any inquiries or support, please contact:
- **Email:** caio@lombello.com

## Using the GPT with GitDoc AI

You can also interact with this API using a pre-configured GPT model. Visit the following link to start using GitDoc AI with GPT:

- [GitDoc AI GPT Interface](https://chatgpt.com/g/g-x15sx8ssK-gitdoc-ai)

This link will take you to a custom GPT interface that uses the GitDoc AI API to provide insights and suggestions based on your GitHub documentation.