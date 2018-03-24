import pytest
from project.fibonacci import fibonacci1, fibonacci2

"""
fib(0) = None
fib(1) = 0
fib(2) = 1
fib(3) = 1
fib(4) = 2
fib(5) = 3
fib(6) = 5
fib(7) = 8
fib(8) = 13
fib(100) = 218922995834555169026
"""
@pytest.mark.parametrize("test_input,expected", [
    (0, None),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (100, 218922995834555169026)
    ])

def test_fibonacci_generator(test_input, expected):
    assert fibonacci1(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    (0, None),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    ])

def test_fibonacci_recursive(test_input, expected):
    assert fibonacci2(test_input) == expected
