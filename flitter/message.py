class Message:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def is_by(self, user):
        return self.author == user

    def mentions(self, user):
        if f'@{user.lower()}' in self.text.lower().split(" "):
            return user
