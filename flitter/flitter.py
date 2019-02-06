from flitter.message import Message


class Flitter:
    def __init__(self, message_store, follow_store):
        self.message_store = message_store
        self.follow_store = follow_store

    def post(self, author, message):
        """
        Post a message

        :param author: The user name of the author
        :type author: string
        :param message: The message to be posted
        :type message: string
        :return: nothing
        :rtype: void
        """

        self.message_store.add(Message(author=author, text=message))

    def get_feed_for(self, user):
        """
        Get messages in a users feed.

        :param user: The user to get messages for
        :type user: string
        :return: All the message in the feed for a given user
        :rtype: list(dict(author=string, message=string))
        """

        feed = self.message_store.fetch_by(user)

        for followee in self.follow_store.get_followees_for(user):
            feed = feed + self.message_store.fetch_by(followee)
        feed = feed + self.message_store.fetch_by_mention(user)
        return [dict(author=msg.author, message=msg.text) for msg in feed]



    def follow(self, follower, followee):
        """
        Make one user follow another
        :param follower: The user who is following
        :type follower: string
        :param followee:  The user being followed
        :type followee: string
        :return: nothing
        :rtype: void
        """

        self.follow_store.add(follower=follower, followee=followee)
