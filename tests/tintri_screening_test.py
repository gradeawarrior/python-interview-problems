"""
Description
===========

Write a simple function that take a input string, add a space after every 3rd character, and
return the modified string
"""

from project.tintri_screening import simple_function
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("foo", "foo"),
    ("jalsdflbvflnvfmdklsdfsdjkbd", "jal sdf lbv fln vfm dkl sdf sdj kbd"),
    ("foobar", "foo bar")])

def test_simplefunction(test_input, expected):
    assert simple_function(test_input) == expected

