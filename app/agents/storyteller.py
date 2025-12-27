from typing import List, Dict
from app.prompts.storyteller_prompt import STORYTELLER_SYSTEM_PROMPT
from app.utils.llm_client import call_model


class StorytellerAgent:
    """
    Conversational storyteller agent.
    Uses conversation history to continue, revise, or create bedtime stories.
    """

    def tell_story(
        self,
        conversation_history: List[Dict[str, str]],
        user_request: str
    ) -> str:
        """
        Generate a story response based on conversation context and user input.
        """

        prompt = self._build_prompt(conversation_history, user_request)

        return call_model(
            prompt,
            temperature=0.85,   # creative
            max_tokens=1400
        ).strip()

    def _build_prompt(
        self,
        conversation_history: List[Dict[str, str]],
        user_request: str
    ) -> str:
        """
        Builds a conversational prompt including prior turns.
        """

        history_text = ""
        for turn in conversation_history:
            role = turn.get("role", "user").capitalize()
            content = turn.get("content", "")
            history_text += f"{role}: {content}\n"

        return f"""
{STORYTELLER_SYSTEM_PROMPT}

You are having a gentle bedtime conversation with a child.
Use the conversation so far to respond naturally.

Conversation so far:
{history_text}

Child says:
{user_request}

Granny responds with a warm, bedtime-appropriate story or continuation:
"""
