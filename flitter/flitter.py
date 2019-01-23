class Flitter:
    def __init__(self):
        self.feed = []

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
        self.feed.append(dict(author=author, message=message))

    def get_feed_for(self, user):
        """
        Get messages in a users feed.

        :param user: The user to get messages for
        :type user: string
        :return: All the message as a list of dicts containing author and message
        :rtype: list(dict(author=string, message=string))
        """
        return self.feed

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
        pass
