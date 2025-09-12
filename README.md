# Symptom Checker

A FastAPI-based symptom checker application powered by OpenAI.

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. Follow these steps to get started:

### Prerequisites

1. **Install uv** (if not already installed):
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akhjunaid0047/symptomchecker
   cd symptomchecker
   ```

2. **Install all dependencies:**
   ```bash
   uv sync
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root and add your configuration:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the Server

```bash
# Activate the virtual environment and run the app
uv run fastapi dev main.py
```

The application will be available at `http://localhost:8000`

## Development

- **Add new dependencies:** `uv add package-name`
- **Add development dependencies:** `uv add --dev package-name`
- **Update dependencies:** `uv sync --upgrade`
- **Run commands in the virtual environment:** `uv run <command>`

## API Documentation

Once running, visit:
- Interactive API docs: `http://localhost:8000/docs`

