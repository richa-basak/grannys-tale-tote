class ConversationState:
    def __init__(self):
        self.history = []
        self.last_story = None

    def add_user_message(self, message: str):
        self.history.append({"role": "user", "content": message})

    def add_story(self, story: str):
        self.history.append({"role": "assistant", "content": story})
        self.last_story = story
