"""
AI Service
Handles message distortion using AI models (or mock responses)
"""
import os
import random
import logging
from typing import Optional
import aiohttp

from app.distortion_modes import DISTORTION_MODES

logger = logging.getLogger(__name__)


class AIService:
    """Handles AI-powered message distortion"""

    def __init__(self):
        self.use_mock = os.getenv("USE_MOCK_AI", "true").lower() == "true"
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = "llama2"  # Default model

    async def distort_message(self, original: str, mode: str = "chaotic") -> str:
        """
        Distort a message based on the selected mode

        Args:
            original: The original message text
            mode: The distortion mode to apply

        Returns:
            The distorted message text
        """
        if self.use_mock:
            return self._mock_distort(original, mode)
        else:
            return await self._ollama_distort(original, mode)

    def _mock_distort(self, original: str, mode: str) -> str:
        """Mock distortion for development/testing"""
        mode_config = DISTORTION_MODES.get(mode, DISTORTION_MODES["chaotic"])

        # Simple mock transformations based on mode
        if mode == "wholesome":
            return self._wholesome_transform(original)
        elif mode == "bureaucratic":
            return self._bureaucratic_transform(original)
        elif mode == "chaotic":
            return self._chaotic_transform(original)
        elif mode == "edgy_teenager":
            return self._edgy_teenager_transform(original)
        elif mode == "corporate_hr":
            return self._corporate_hr_transform(original)
        else:
            return original

    def _wholesome_transform(self, text: str) -> str:
        """Make message overly positive and wholesome"""
        wholesome_additions = [
            f"{text} 🌈✨ You're doing amazing!",
            f"What a wonderful thing to say! {text} Have a blessed day!",
            f"{text} Sending you positive vibes and virtual hugs! 🤗💕",
            f"This brightened my day: {text} You're such a kind soul!",
        ]
        return random.choice(wholesome_additions)

    def _bureaucratic_transform(self, text: str) -> str:
        """Transform into corporate bureaucratic speak"""
        templates = [
            f"RE: {text}\n\nPlease be advised that per company policy §4.2.7, the aforementioned statement has been logged. Follow-up pending.",
            f"MEMORANDUM\nFROM: Communications Dept\nRE: Message Receipt\n\nYour message '{text}' has been received and is currently under review. Please allow 3-5 business days for processing.",
            f"As per our discussion: {text}\n\nAction Items:\n- Review message content\n- Escalate to stakeholders\n- Schedule follow-up meeting\n\nCC: All concerned parties",
        ]
        return random.choice(templates)

    def _chaotic_transform(self, text: str) -> str:
        """Randomly misinterpret or exaggerate the message"""
        chaos_templates = [
            f"BREAKING: {text.upper()}!!! THIS CHANGES EVERYTHING!!!",
            f"did u just say {random.choice(['WHAT', 'huh???', 'wait WHAT', 'no way'])} - {text}???",
            f"{text}... or did you mean the COMPLETE OPPOSITE? 🤔",
            f"URGENT: {text} [citation needed] [disputed] [probably fake news]",
            f"*whispers* {text} *runs away screaming*",
            f"{text}????????? okay but WHY THO",
        ]
        return random.choice(chaos_templates)

    def _edgy_teenager_transform(self, text: str) -> str:
        """Transform into angsty teenage speak"""
        edgy_templates = [
            f"ugh whatever... {text} 🙄",
            f"{text} i guess... if u even CARE",
            f"nobody:\nabsolutely nobody:\nme: {text}",
            f"{text}\n\n*goes back to listening to my chemical romance*",
            f"lol imagine thinking '{text}' matters",
        ]
        return random.choice(edgy_templates)

    def _corporate_hr_transform(self, text: str) -> str:
        """Transform into HR-approved corporate speak"""
        hr_templates = [
            f"Thank you for sharing that perspective. Re: '{text}' - let's take this offline and circle back to align on best practices moving forward.",
            f"I appreciate you bringing this to my attention. '{text}' presents an opportunity for synergy. Let's touch base to leverage our collective bandwidth.",
            f"Per our core values, I'd like to acknowledge: {text}. This demonstrates great thought leadership. Let's put a pin in this for our next alignment session.",
            f"Thanks for your input regarding '{text}'. To ensure we're all rowing in the same direction, let's schedule a town hall to deep-dive into this.",
        ]
        return random.choice(hr_templates)

    async def _ollama_distort(self, original: str, mode: str) -> str:
        """Use real Ollama API for distortion"""
        mode_config = DISTORTION_MODES.get(mode, DISTORTION_MODES["chaotic"])
        prompt = mode_config["system_prompt"].format(message=original)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.ollama_base_url}/api/chat",
                    json={
                        "model": self.model,
                        "messages": [
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        "stream": False
                    },
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result.get("message", {}).get("content", original)
                    else:
                        logger.error(f"Ollama API error: {response.status}")
                        return self._mock_distort(original, mode)
        except Exception as e:
            logger.error(f"Error calling Ollama API: {e}")
            return self._mock_distort(original, mode)
