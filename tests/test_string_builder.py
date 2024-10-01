from lib.string_builder import *

def test_string_test_empty():
    builder = StringBuilder()
    assert builder.output() == ""

def test_string_test_add():
    builder = StringBuilder()
    builder.add("Hi, how are you?")
    assert builder.size() == 16

def test_string_test_return():
    builder = StringBuilder()
    builder.add("apple, banana, cantaloupe, dragon fruit")
    assert builder.output() == "apple, banana, cantaloupe, dragon fruit"