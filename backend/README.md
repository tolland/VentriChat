# VentriChat Backend

FastAPI backend with WebSocket support and AI message distortion.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- [hatch](https://hatch.pypa.io/) - Modern Python project manager (`pipx install hatch`)

## Setup

```bash
# Install dependencies with uv
uv sync

# Configure environment
cp .env.example .env
```

## Running

```bash
# Development mode with auto-reload
hatch run dev

# Production mode
hatch run start
```

The server will start on `http://localhost:8000`

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Environment Variables

- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 8000)
- `OLLAMA_BASE_URL` - Ollama API URL (default: http://localhost:11434)
- `USE_MOCK_AI` - Use mock AI responses (default: true)

## Development Commands

```bash
# Run development server with auto-reload
hatch run dev

# Run tests
hatch run test

# Check code formatting and linting
hatch run lint:check

# Auto-format code
hatch run lint:format
```

## Architecture

- `main.py` - FastAPI application and WebSocket endpoint
- `app/websocket_manager.py` - WebSocket connection management
- `app/ai_service.py` - AI message distortion logic
- `app/distortion_modes.py` - Configuration for distortion modes
- `app/routes/chat.py` - Chat-related REST endpoints
- `app/routes/mock_ollama.py` - Mock Ollama API for development
- `pyproject.toml` - Project configuration and dependencies (hatch/uv)
