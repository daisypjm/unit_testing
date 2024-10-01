from lib.greet import *

def test_greet_returns_daisy_for_daisy():
    result = greet("Daisy")
    assert result == "Hello, Daisy!"


def test_greet_returns_stranger_for_string():
    result = greet("Stranger")
    assert result == "Hello, Stranger!"

def test_greet_returns_ghosts_for_string():
    result = greet("who's there??")
    assert result == "Hello, who's there??!"

