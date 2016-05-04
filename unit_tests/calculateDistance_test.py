import pytest

from main import calculateDistance

#make initial test pass. ensure correct value is returned
def test_example_1():
    assert calculateDistance(4, 6, 1, 6) == 3
    
    
#if one of the values is too large ( > 1000000000 )
def test_example_2():
    assert calculateDistance(100000000000000000, 2, 4, 5) == "One of your values is too large. x and y values must be <= 1000000000."
    
#if one of the values is not numeric
def test_example_3():
    assert calculateDistance(5, 2, "str", 5) == "One of your values is not numeric. x and y values must be either an integer or float."
    
#ensure function also works for float values
def test_example_4():
    assert calculateDistance(4.0, 6.0, 1.0, 6.0) == 3.0
    
#if one of the values is too small ( < 1000000000 )
def test_example_5():
    assert calculateDistance(-100000000000000000, 2, 4, 5) == "One of your values is too small. x and y values must be >= -1000000000."
