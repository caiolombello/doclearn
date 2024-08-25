# DocLearn

This project is a Python application that provides an interface to interact with the GitHub API, allowing operations such as listing Markdown files, retrieving content, and listing branches and tags of a repository.

## Overview

The main objective of the project is to allow users to perform GitHub-related operations in a simple and efficient manner. The application is divided into two main parts: the API, which manages routes and requests, and the business logic, which contains the core functionalities of the project.

## Project Structure

- **`main.py`**: Entry point of the application.
- **`api/`**: Contains the implementation of API routes.
  - **`routes.py`**: Defines routes and request handlers.
- **`core/`**: Contains the business logic and main functionalities.
  - **`filters.py`**: Implements filters for processing data.
  - **`github_client.py`**: Manages communication with the GitHub API.
- **`docs/`**: Contains project documentation.
  - **`introduction.md`**: Project overview, requirements, and execution instructions.

## Requirements

- Python 3.x
- [uv](https://astral.sh/uv/) for managing and executing the environment.

## Installation and Execution

### Step 1: Clone the Repository

Clone the repository to your local machine using the command:

```bash
git clone https://github.com/caiolombello/doclearn.git
cd doclearn
```


### Step 2: Install and Configure uv

Install `uv` following the instructions below:

#### For macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


#### For Windows:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```


### Step 3: Create Virtual Environment with uv

Create a virtual environment using `uv`:

```bash
uv -n project_name
```


Activate the created virtual environment:

```bash
uv
```


### Step 4: Install Dependencies

Install the necessary dependencies within the `uv` environment:

```bash
uv run pip install -r requirements.txt
```


### Step 5: Run the Application

Start the application:

```bash
uv run python main.py
```


The application will be available at `http://localhost:8000`.

## Usage

The application exposes a series of endpoints to interact with the GitHub API. See the [documentation](src/doclearn/docs/code/introduction.md) for more details on how to use these endpoints.

## License

This project is licensed under the [MIT License](LICENSE).

## Contribution

Contributions are welcome! If you wish to contribute, please fork the repository, create a branch for your changes, and submit a pull request.