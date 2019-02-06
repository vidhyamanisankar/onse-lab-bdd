class InMemoryMessageStore:
    def __init__(self):
        self.messages = []

    def add(self, message):
        self.messages.append(message)

    def fetch_by(self, user):
        return [message for message in self.messages if message.is_by(user)]

    def fetch_by_mention(self, user):
        return [message for message in self.messages if message.mentions(user)]

