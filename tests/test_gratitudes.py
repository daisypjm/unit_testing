from lib.gratitudes import *

# is gratitudes list empty?

def test_empty_string():
    grateful = Gratitudes()
    assert grateful.gratitudes == []

# do multiple gratitudes concatenate correctly?

def test_multiple_gratitudes_concat():
    grateful = Gratitudes()
    grateful.add("my friends")
    grateful.add("my family")
    assert grateful.gratitudes == ["my friends", "my family"]

# do multiple gratitudes format correctly?

def test_multiple_gratitudes_concat_two():
    grateful = Gratitudes()
    grateful.add("my friends")
    grateful.add("my family")
    assert grateful.format() == "Be grateful for: my friends, my family"