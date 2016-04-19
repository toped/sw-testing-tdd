import pytest

from main import calculateBMI

def test_example_1():
    assert calculateBMI(5, 3, 125) == 22.7
