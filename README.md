# Project Setup Guide

This document provides step-by-step instructions to set up and run the project.

## Prerequisites

- [Git](https://git-scm.com/)
- [uv](https://github.com/astral-sh/uv) (Python package/dependency manager)
- Python 3.8 or higher

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sharjeel-ahmed17/agentic_ai_task.git
    cd agentic_ai_task
    ```

2. **Create and activate a virtual environment:**
    ```bash
    uv venv
    .venv\Scripts\activate  # On Windows
    # or
    source .venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies:**
    ```bash
    uv sync
    ```

## Configuration

1. **Rename the environment file:**
    - Rename `.env.example` to `.env`.

2. **Obtain Gemini API Key:**
    - Visit [Google AI Studio](https://aistudio.google.com/) and generate an API key.
    - Add your API key to the `.env` file:
      ```
      GEMINI_API_KEY=your_gemini_api_key_here
      ```

## Running the Project

Use the following commands to run different modules:

```bash
uv run chainlit run .\bot.py
uv run .\main.py
uv run .\run.py
uv run .\global.py
uv run .\agent.py
```

> **Note:** Ensure your virtual environment is activated before running these commands.

## Troubleshooting

- If you encounter issues, verify your Python version and that all dependencies are installed.
- Check that your `.env` file contains a valid API key.

## License

This project is licensed under the MIT License.

