from behave import given, when, then


@given('{author} has posted a message "{message}"')
def post_message(context, author, message):
    context.app.post(author=author, message=message)


@given('{follower} follows {followee}')
def follow(context, follower, followee):
    raise NotImplementedError(context.errorMessage)


@given('{follower} is not following {followee}')
def do_not_follow(context, follower, followee):
    raise NotImplementedError(context.errorMessage)


@when('{user} views their feed')
def view_feed(context, user):
    context.feed = context.app.get_feed_for(user)


@then('they can see the message "{message}" by {author}')
def assert_can_see_message(context, message, author):
    assert dict(author=author, message=message) in context.feed


@then('they cannot see the message "{message}" by {author}')
def assert_cannot_see_message(context, message, author):
    raise NotImplementedError(context.errorMessage)
