# TODO
"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:
- Persist conversation state across sessions
- Add parent controls and bedtime modes (calm / playful)
- Add memory trimming and stronger safety validation
"""

from app.pipeline.story_loop import StoryLoop
from app.state.conversation import ConversationState


def main():
    EXIT_PHRASES = {
        "bye",
        "bye bye",
        "byee",
        "tata",
        "gtg",
        "got to go now",
        "enough",
        "stop",
        "ok bye",
        "good night",
        "goodnight",
        "night",
        "exit",
        "quit",
    }

    print("\n🧶 Granny’s Tote of Tiny Tales")
    print("Talk to Granny! Type 'goodnight' to end.\n")

    loop = StoryLoop()
    state = ConversationState()

    while True:
        user_input = input("You: ").strip().lower()

        if any(phrase in user_input for phrase in EXIT_PHRASES):
            print("\nGranny: Sleep tight, dear 🌙")
            break

        response = loop.run_turn(state, user_input)

        print("\nGranny:")
        print(response)
        print()


if __name__ == "__main__":
    main()
