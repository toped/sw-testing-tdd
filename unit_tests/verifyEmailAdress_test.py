# coding=utf-8
"""
Assignment 4: Test Driven Development and Unit Testing


email criteria: (i.e., some_string1 ‘@’ some_string2 ‘.’ some_string3 that’s 3 letters or less) ­ can assume some_string1 and some_string2 are made up of any alphanumeric character or symbol ­ some_string3 must be less than 3 letters.
"""

import pytest

from main import verifyEmailAddress


def test_valid_email():
    assert verifyEmailAddress("hds109@msstate.ed") == True

def test_input_with_multiple_at_symbols():
    assert verifyEmailAddress("hds@109@msstate.ed") == False
    assert verifyEmailAddress("hds109@@msstate.ed") == False