import pytest

#import pytest

# import code

from lib.password_checker import *

# test 8 or more characters, True

def test_eight_or_more():
    password = PasswordChecker()
    result = password.check("qwerty1234")
    assert result == True


# test under 8 characters, error message

def test_under_eight():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("qwerty")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."   

# test weird characters

def test_weird_characters():
    password = PasswordChecker()
    result = password.check("!@£$%^&*()hellolalala")
    assert result == True
