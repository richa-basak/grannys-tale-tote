import json
from app.prompts.judge_prompt import JUDGE_SYSTEM_PROMPT
from app.utils.llm_client import call_model


class JudgeAgent:
    def evaluate(self, story: str) -> dict:
        prompt = f"{JUDGE_SYSTEM_PROMPT}\n\nStory to evaluate:\n{story}\n\nReturn ONLY JSON:"
        raw = call_model(prompt, temperature=0.2, max_tokens=600).strip()

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {
                "overall_score": 0,
                "issues": ["Judge returned invalid JSON."],
                "improvement_suggestions": ["Try again and return ONLY valid JSON."],
            }
