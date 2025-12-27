from enum import Enum

class Intent(Enum):
    NEW_STORY = "new_story"
    MODIFY_STORY = "modify_story"


def detect_intent(user_input: str) -> Intent:
    user_input = user_input.lower()

    modification_keywords = [
        "change",
        "make it",
        "shorter",
        "longer",
        "add",
        "remove",
        "different",
    ]

    if any(word in user_input for word in modification_keywords):
        return Intent.MODIFY_STORY

    return Intent.NEW_STORY
