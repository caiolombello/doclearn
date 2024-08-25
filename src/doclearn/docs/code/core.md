---
title: core
description: 'Main directory containing the project's central logic, including filters and GitHub integration.'
---

# core

The `core` directory is responsible for housing the central logic of the project. It contains modules that implement essential functionalities, such as data filters and communication with the GitHub API.

## Directory Structure

- **filters.py**: This module contains functions and classes that apply filters to data, allowing for the manipulation and extraction of relevant information.
  
- **github_client.py**: This module is responsible for integration with the GitHub API, facilitating operations such as authentication, data requests, and repository manipulation.

## Considerations

The organization of the `core` directory is fundamental for the maintenance and scalability of the project. Each module should be designed to be reusable and testable, ensuring that the central logic remains clear and efficient.