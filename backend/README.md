# VentriChat Backend

FastAPI backend with WebSocket support and AI message distortion.

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
```

## Running

```bash
python main.py
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

## Architecture

- `main.py` - FastAPI application and WebSocket endpoint
- `app/websocket_manager.py` - WebSocket connection management
- `app/ai_service.py` - AI message distortion logic
- `app/distortion_modes.py` - Configuration for distortion modes
- `app/routes/chat.py` - Chat-related REST endpoints
- `app/routes/mock_ollama.py` - Mock Ollama API for development
