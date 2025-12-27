from app.agents.storyteller import StorytellerAgent
from app.agents.judge import JudgeAgent
from app.state.conversation import ConversationState
from app.utils.intent import detect_intent, Intent

QUALITY_THRESHOLD = 8
MAX_REVISIONS = 2


class StoryLoop:
    """
    Orchestrates conversational storytelling with:
    - intent detection (new story vs modification)
    - a storyteller agent
    - a judge agent for quality & safety
    """

    def __init__(self):
        self.storyteller = StorytellerAgent()
        self.judge = JudgeAgent()

    def run_turn(self, state: ConversationState, user_input: str) -> str:
        """
        Handle a single conversational turn.
        """
        # 1. Record user input
        state.add_user_message(user_input)

        # 2. Detect intent
        intent = detect_intent(user_input)

        # 3. Build prompt strategy
        if intent == Intent.NEW_STORY or state.last_story is None:
            storyteller_input = user_input
        else:
            storyteller_input = self._build_modification_prompt(
                state.last_story,
                user_input
            )

        # 4. Generate initial story / revision
        story = self.storyteller.tell_story(
            conversation_history=state.history,
            user_request=storyteller_input,
        )

        # 5. Judge + refinement loop
        revisions = 0
        while revisions < MAX_REVISIONS:
            evaluation = self.judge.evaluate(story)
            score = evaluation.get("overall_score", 0)

            if score >= QUALITY_THRESHOLD:
                break

            suggestions = evaluation.get("improvement_suggestions", [])
            revision_prompt = self._build_revision_prompt(story, suggestions)

            story = self.storyteller.tell_story(
                conversation_history=state.history,
                user_request=revision_prompt,
            )

            revisions += 1

        # 6. Record assistant response
        state.add_story(story)

        return story

    # ------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------

    def _build_modification_prompt(self, story: str, user_request: str) -> str:
        """
        Prompt used when the user wants to modify an existing story.
        """
        return f"""
Here is the current bedtime story:
{story}

The child asks:
{user_request}

Please gently revise the story while:
- keeping the same characters and setting
- preserving a calm, bedtime tone
- remaining appropriate for ages 5–10
- ending with warmth and reassurance
"""

    def _build_revision_prompt(self, story: str, suggestions: list) -> str:
        """
        Prompt used when the judge requests improvements.
        """
        suggestions_text = (
            "\n".join(f"- {s}" for s in suggestions)
            if suggestions
            else "- Make the story calmer and clearer."
        )

        return f"""
Please gently revise the bedtime story below for a child aged 5–10.

Apply the following feedback:
{suggestions_text}

The story must:
- follow a clear story arc (setup → gentle challenge → resolution → warm ending)
- remain emotionally safe and bedtime-appropriate
- use simple, comforting language
- end with a gentle lesson

Story:
{story}
"""
