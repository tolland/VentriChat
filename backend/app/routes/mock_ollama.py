"""
Mock Ollama API
Simulates Ollama's API for self-contained development/testing
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import random

from app.ai_service import AIService

router = APIRouter()


class GenerateRequest(BaseModel):
    """Ollama generate request format"""
    model: str
    prompt: str
    stream: bool = False


class GenerateResponse(BaseModel):
    """Ollama generate response format"""
    model: str
    response: str
    done: bool = True


@router.post("/generate")
async def mock_generate(request: GenerateRequest) -> GenerateResponse:
    """
    Mock Ollama /api/generate endpoint
    This allows VentriChat to run completely self-contained
    """
    ai_service = AIService()

    # Extract mode from prompt if possible, otherwise use chaotic
    mode = "chaotic"
    for mode_key in ["wholesome", "bureaucratic", "chaotic", "edgy_teenager", "corporate_hr", "paranoid", "pirate", "shakespearean"]:
        if mode_key.replace("_", " ") in request.prompt.lower():
            mode = mode_key
            break

    # Extract original message from prompt
    # The prompt should contain the message after "Message: "
    message = ""
    if "Message: " in request.prompt:
        message = request.prompt.split("Message: ")[-1].strip()
    else:
        message = request.prompt

    # Use mock distortion
    ai_service.use_mock = True
    distorted = ai_service._mock_distort(message, mode)

    return GenerateResponse(
        model=request.model,
        response=distorted,
        done=True
    )


@router.get("/tags")
async def mock_tags():
    """Mock Ollama /api/tags endpoint"""
    return {
        "models": [
            {
                "name": "llama2:latest",
                "modified_at": "2024-01-15T00:00:00Z",
                "size": 3826793677
            }
        ]
    }
