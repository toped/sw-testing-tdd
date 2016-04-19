import pytest

from main import calculateRetirement


def test_example_1():
    assert calculateRetirement(20, 50000, 20, 100000) == 25