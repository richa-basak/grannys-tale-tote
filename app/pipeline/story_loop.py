from app.agents.storyteller import StorytellerAgent
from app.agents.judge import JudgeAgent

QUALITY_THRESHOLD = 8
MAX_REVISIONS = 2


class StoryLoop:
    def __init__(self):
        self.storyteller = StorytellerAgent()
        self.judge = JudgeAgent()

    def run(self, user_prompt: str) -> dict:
        story = self.storyteller.tell_story(user_prompt)
        final_score = 0
        revisions = 0

        while revisions <= MAX_REVISIONS:
            evaluation = self.judge.evaluate(story)
            final_score = evaluation.get("overall_score", 0)

            if final_score >= QUALITY_THRESHOLD:
                break

            suggestions = evaluation.get("improvement_suggestions", [])
            story = self.storyteller.tell_story(self._revision_prompt(story, suggestions))
            revisions += 1

        return {
            "final_story": story,
            "final_score": final_score,
            "revisions": revisions,
        }

    def _revision_prompt(self, story: str, suggestions: list) -> str:
        suggestions_text = "\n".join(f"- {s}" for s in suggestions) if suggestions else "- Make it calmer and clearer."
        return f"""
Revise the bedtime story below for ages 5–10.

Must be:
- gentle and bedtime-calm
- emotionally safe
- simple language
- clear beginning/middle/end
- happy ending + gentle lesson

Judge feedback to apply:
{suggestions_text}

Story:
{story}
"""
