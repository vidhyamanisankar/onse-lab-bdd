from flitter.message import Message


def test_is_by_checks_if_author_matches_user():
    message = Message(author='charlie', text='hello')

    assert message.is_by('charlie')
    assert not message.is_by('bob')


def test_user_is_mentioned_in_message():
    message = Message(author='alice', text='I like @Bob')

    assert message.mentions('Bob') == 'Bob'


def test_user_does_not_match_similar_username():
    message = Message(author='alice', text='I like @BobHope')

    assert not message.mentions('Bob')


def test_different_case_matches_user():
    message = Message(author='alice', text='I like @bOb')

    assert message.mentions('Bob')
