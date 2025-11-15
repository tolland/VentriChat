"""
WebSocket Connection Manager
Handles real-time connections and message broadcasting
"""
from fastapi import WebSocket
from typing import Dict, List
import logging
from datetime import datetime

from app.ai_service import AIService

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections and message routing"""

    def __init__(self):
        # Room-based connections: {room_id: {username: WebSocket}}
        self.active_connections: Dict[str, Dict[str, WebSocket]] = {}
        self.ai_service = AIService()

    async def connect(self, websocket: WebSocket, room_id: str, username: str):
        """Accept and register a new WebSocket connection"""
        await websocket.accept()

        if room_id not in self.active_connections:
            self.active_connections[room_id] = {}

        self.active_connections[room_id][username] = websocket
        logger.info(f"User {username} connected to room {room_id}")

        # Notify room about new user
        await self.broadcast_to_room(
            room_id,
            {
                "type": "user_joined",
                "username": username,
                "timestamp": datetime.utcnow().isoformat(),
                "users_count": len(self.active_connections[room_id])
            }
        )

    async def disconnect(self, room_id: str, username: str):
        """Remove a WebSocket connection"""
        if room_id in self.active_connections:
            if username in self.active_connections[room_id]:
                del self.active_connections[room_id][username]

                # Notify room about user leaving
                await self.broadcast_to_room(
                    room_id,
                    {
                        "type": "user_left",
                        "username": username,
                        "timestamp": datetime.utcnow().isoformat(),
                        "users_count": len(self.active_connections[room_id])
                    }
                )

                # Clean up empty rooms
                if not self.active_connections[room_id]:
                    del self.active_connections[room_id]

    async def handle_message(self, data: dict, room_id: str, username: str):
        """Process incoming message and broadcast AI-distorted version"""
        message_type = data.get("type", "message")

        if message_type == "message":
            original_text = data.get("text", "")
            mode = data.get("mode", "chaotic")

            # Get AI-distorted version
            distorted_text = await self.ai_service.distort_message(
                original_text,
                mode
            )

            # Broadcast to room
            await self.broadcast_to_room(
                room_id,
                {
                    "type": "message",
                    "username": username,
                    "original": original_text,
                    "distorted": distorted_text,
                    "mode": mode,
                    "timestamp": datetime.utcnow().isoformat()
                }
            )

    async def broadcast_to_room(self, room_id: str, message: dict):
        """Send message to all connections in a room"""
        if room_id not in self.active_connections:
            return

        disconnected_users = []

        for username, connection in self.active_connections[room_id].items():
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error sending to {username}: {e}")
                disconnected_users.append(username)

        # Clean up disconnected users
        for username in disconnected_users:
            await self.disconnect(room_id, username)

    def get_room_users(self, room_id: str) -> List[str]:
        """Get list of users in a room"""
        if room_id in self.active_connections:
            return list(self.active_connections[room_id].keys())
        return []


# Global manager instance
manager = ConnectionManager()
