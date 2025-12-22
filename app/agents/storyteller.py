from app.prompts.storyteller_prompt import STORYTELLER_SYSTEM_PROMPT
from app.utils.llm_client import call_model


class StorytellerAgent:
    def tell_story(self, user_request: str) -> str:
        prompt = f"{STORYTELLER_SYSTEM_PROMPT}\n\nUser request:\n{user_request}\n\nNow write the story:"
        return call_model(prompt, temperature=0.85, max_tokens=1400).strip()
