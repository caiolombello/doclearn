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

## Usage

### API Endpoints

- **GET `/markdowns/`**: Lists Markdown files in a repository with filtering options.
- **GET `/markdowns/{file_path:path}`**: Retrieves the content of a specific Markdown file.
- **GET `/markdowns/all/`**: Fetches the content of all Markdown files in a repository.
- **GET `/branches/`**: Lists all branches in a repository.
- **GET `/tags/`**: Lists all tags in a repository.

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