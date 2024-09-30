from lib.greet import *

def test_greet_returns_daisy_for_daisy():
    result = greet("Daisy")
    assert result == "Hello, Daisy!"
