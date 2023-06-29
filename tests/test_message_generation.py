
from app.service import get_customized_message

def test_get_customized_messages():
    """
    In this test, we are testing the get_customized_message() function from app/service.py

    We'd like to assert that the function doesn't return the same message every time.

    The way we do this is by calling the function twice and asserting that the two messages are not equal.
    But, the function can accidentally return the same message twice, so we should call the function
    many times and assert that the messages are not equal every time.

    In this test, the function is called 10 times. 

    If the function returns the same message every time, the test will fail.
    If there are at least two unique messages, the test will pass.

    In the last line of code, we use the "set" data structure to get the number of unique messages.
    https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
    """
    messages = []
    for i in range(10):
        messages.append(get_customized_message())
    assert len(set(messages)) > 1 
