import pytest

from main import calculateDistance


def test_example_1():
    assert calculateDistance(4, 6, 1, 6) == 3