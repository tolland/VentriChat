"""
Chat API Routes
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from app.distortion_modes import get_available_modes
from app.websocket_manager import manager

router = APIRouter()


class ChatRoom(BaseModel):
    """Chat room information"""
    room_id: str
    user_count: int
    users: List[str]


@router.get("/modes")
async def get_modes():
    """Get available AI distortion modes"""
    return {
        "modes": get_available_modes()
    }


@router.get("/rooms/{room_id}")
async def get_room_info(room_id: str) -> ChatRoom:
    """Get information about a chat room"""
    users = manager.get_room_users(room_id)
    return ChatRoom(
        room_id=room_id,
        user_count=len(users),
        users=users
    )


@router.get("/rooms")
async def list_rooms():
    """List all active chat rooms"""
    rooms = []
    for room_id in manager.active_connections.keys():
        users = manager.get_room_users(room_id)
        rooms.append({
            "room_id": room_id,
            "user_count": len(users),
            "users": users
        })
    return {"rooms": rooms}
