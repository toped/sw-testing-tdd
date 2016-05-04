import pytest

from main import calculateRetirement


# test for expected basic functionality
def test_expected_outcome():
    assert calculateRetirement(20, 50000, 20, 100000) == 30

# test that a retirement age >=100 will notify the user
def test_goal_not_met():
    assert calculateRetirement(40, 20000, 20, 500000) == "You will not meet your savings goal"

# test if an age is entered which already exceeds max age
def test_age():
    assert calculateRetirement(100, 20000, 20, 500000) == "The age you entered is too high.  You shouldn't be working!"
