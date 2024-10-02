import pytest

from lib.house import *

# When we build a new house
# It needs to be given a house number and starting door colour
# Those and the number of floors are stored in attributes

def test_starting_attributes():
    house = House(137, "white")
    assert house.floors == 2
    assert house.number == 137
    assert house.door_colour == "white"


# When we have a house
# The key details can be got back

def test_detail_return():
    house = House(137, "white")
    assert house.house_details() == "House number 137 has 2 floors and a white door"

# When we have a house
# And we change its door colour
# This is reflected in its attribute

def test_changing_doors():
    house = House(24, "red")
    house.repaint_door("blue")
    assert house.door_colour == "blue"
