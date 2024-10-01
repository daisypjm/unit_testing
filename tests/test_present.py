#import pytest to test the exceptions

import pytest

# import the code we want to test

from lib.present import *

# test wrapping no presents

def test_wrapping_no_presents():
    present = Present()
    present.wrap(None)
    assert present.contents == None

# test wrapping presents, and returning when unwrapped

def test_wrapping_and_unwrapping():
    present = Present()
    present.wrap(5)
    assert present.unwrap() == 5

# test wrapping no presents, and returning error when unwrapped

def test_unwrapping_no_presents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

# test wrapping multiple presents

def test_wrapping_multiple_presents():
    present = Present()
    present.wrap(5)
    with pytest.raises(Exception) as e:
        present.wrap(2)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

# test wrapping twice keeps first value

def test_wrapping_twice_preserves_first():
    present = Present()
    present.wrap(5)
    with pytest.raises(Exception) as e:
        present.wrap(2)
    assert present.unwrap() == 5

