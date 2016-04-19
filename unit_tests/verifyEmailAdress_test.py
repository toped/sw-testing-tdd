import pytest

from main import verifyEmailAddress


def test_example_1():
    assert verifyEmailAddress("hds109.msstate.edu") == True