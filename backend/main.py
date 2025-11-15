"""
VentriChat Backend
Main FastAPI application with WebSocket support
"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import os
from dotenv import load_dotenv

from app.websocket_manager import manager
from app.routes import chat, mock_ollama

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    logger.info("VentriChat backend starting up...")
    yield
    logger.info("VentriChat backend shutting down...")


# Create FastAPI app
app = FastAPI(
    title="VentriChat API",
    description="Backend for VentriChat - AI-distorted messaging",
    version="0.1.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(mock_ollama.router, prefix="/api/mock", tags=["mock"])


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "VentriChat",
        "version": "0.1.0",
        "mock_mode": os.getenv("USE_MOCK_AI", "true") == "true"
    }


@app.websocket("/ws/{room_id}/{username}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, username: str):
    """WebSocket endpoint for real-time chat"""
    await manager.connect(websocket, room_id, username)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.handle_message(data, room_id, username)
    except WebSocketDisconnect:
        await manager.disconnect(room_id, username)
        logger.info(f"User {username} disconnected from room {room_id}")


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )
