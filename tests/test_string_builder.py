from lib.string_builder import *

def string_test_add():
    builder = StringBuilder()
    builder.add("Hi, how are you?")
    result = builder.size()
    assert result == 16

def string_test_return():
    builder = StringBuilder()
    builder.add("Hi, how are you?")
    result = builder.output()
    assert result == "Hi, how are you?"