from lib.counter import *

def test_adding_to_counter():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_adding_to_counter_again():
    counter = Counter()
    counter.add(20)
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 30 so far."

def test_adding_to_counter_minus():
    counter = Counter()
    counter.add(-5)
    result = counter.report()
    assert result == "Counted to -5 so far."