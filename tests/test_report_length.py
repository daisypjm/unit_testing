from lib.report_length import *

def test_length_as_simple_string():
    result = report_length("howdy")
    assert result == "This string was 5 characters long."

def test_length_as_int():
    result = report_length("123456789")
    assert result == "This string was 9 characters long."

def test_length_as_complex_string():
    result = report_length("Hello, my name is Barbara Stevens.")
    assert result == "This string was 34 characters long."
