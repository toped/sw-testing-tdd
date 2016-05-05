import pytest

from main import calculateBMI

#test with integers
def test_int():
    assert calculateBMI(5, 3, 125) == "Your body mass index is: 22.6757369615. You are of normal weight."

#test with alphabetic values    
def test_invalid_height_feet():
    assert calculateBMI('a', 3, 150) == "Please enter numeric values."
    
def test_invalid_height_inces():
    assert calculateBMI(3, 'a', 140) == "Please enter numeric values."
    
def test_invalid_weight():
    assert calculateBMI(4, 20, 'a') == "Please enter numeric values."

#test with floats    
def test_float():
    assert calculateBMI(4.0, 20.9, 130) == "Your body mass index is: 19.7168442095. You are of normal weight."
    
