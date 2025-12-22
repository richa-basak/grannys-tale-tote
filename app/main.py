# TODO
"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:
- Add user feedback iteration (e.g., 'shorter', 'more animals', 'calmer')
- Add age tuning (5–7 vs 8–10 vocabulary) and length presets
- Add stronger output validation (length, bedtime tone, forbidden themes) + better JSON-repair for judge
"""

from app.pipeline.story_loop import StoryLoop


def main():
    user_input = input("What kind of story do you want to hear? ")

    loop = StoryLoop()
    result = loop.run(user_input)

    print("\n📖 Your Bedtime Story:\n")
    print(result["final_story"])
    print("\n✨ Details:")
    print(f"Judge Score: {result['final_score']}/10")
    print(f"Revisions: {result['revisions']}")


if __name__ == "__main__":
    main()
