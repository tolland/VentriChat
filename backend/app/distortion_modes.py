"""
Distortion Modes Configuration
Defines different AI "speaker personalities" for message transformation
"""

DISTORTION_MODES = {
    "wholesome": {
        "name": "Wholesome Overload",
        "description": "Transforms everything into overly positive, saccharine sweetness",
        "system_prompt": "Rewrite the following message to be extremely positive, wholesome, and uplifting. Add encouraging words and wholesome emojis. Message: {message}"
    },
    "bureaucratic": {
        "name": "Corporate Bureaucrat",
        "description": "Converts casual messages into formal corporate memorandums",
        "system_prompt": "Rewrite the following message as if it's an official corporate memo or email with formal language, policy references, and bureaucratic jargon. Message: {message}"
    },
    "chaotic": {
        "name": "Chaotic Neutral",
        "description": "Randomly misinterprets, exaggerates, or adds confusion",
        "system_prompt": "Rewrite the following message in a chaotic, unpredictable way. Misinterpret it, exaggerate it, or add confusion. Be creative and unexpected. Message: {message}"
    },
    "edgy_teenager": {
        "name": "Edgy Teenager",
        "description": "Rewrites messages as angsty teenage expressions",
        "system_prompt": "Rewrite the following message as if an edgy, dramatic teenager wrote it. Use teenage slang, add eye-rolls, and make it overly dramatic. Message: {message}"
    },
    "corporate_hr": {
        "name": "HR Department",
        "description": "Sanitizes everything into HR-approved corporate speak",
        "system_prompt": "Rewrite the following message using corporate HR buzzwords and jargon. Make it sound like it came from a Human Resources department memo. Use phrases like 'synergy', 'circle back', 'touch base', etc. Message: {message}"
    },
    "paranoid": {
        "name": "Paranoid Conspiracy",
        "description": "Interprets innocent messages as suspicious or conspiratorial",
        "system_prompt": "Rewrite the following message as if you're paranoid and see hidden meanings everywhere. Add conspiracy theories and suspicious interpretations. Message: {message}"
    },
    "pirate": {
        "name": "Pirate Translator",
        "description": "Translates messages into pirate speak",
        "system_prompt": "Rewrite the following message in pirate speak. Use pirate vocabulary, 'arr', 'matey', nautical terms, etc. Message: {message}"
    },
    "shakespearean": {
        "name": "Shakespearean",
        "description": "Transforms messages into Elizabethan English",
        "system_prompt": "Rewrite the following message in Shakespearean English, as if it were from a play by William Shakespeare. Use 'thee', 'thou', 'hath', and flowery language. Message: {message}"
    }
}


def get_available_modes():
    """Return list of available distortion modes with metadata"""
    return [
        {
            "id": mode_id,
            "name": config["name"],
            "description": config["description"]
        }
        for mode_id, config in DISTORTION_MODES.items()
    ]
