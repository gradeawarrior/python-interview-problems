import pytest
from project.two_sums_bst import Solution, listToTreeNode


@pytest.mark.parametrize("test_input, k, expected", [
    ([5,3,6,2,4,6,7], 4,   False),
    ([5,3,6,2,4,6,7], 5,   True),
    ([5,3,6,2,4,6,7], 6,   True),
    ([5,3,6,2,4,6,7], 7,   True),
    ([5,3,6,2,4,6,7], 8,   True),
    ([5,3,6,2,4,6,7], 9,   True),
    ([5,3,6,2,4,6,7], 10,  True),
    ([5,3,6,2,4,6,7], 11,  True),
    ([5,3,6,2,4,6,7], 12,  True),
    ([5,3,6,2,4,6,7], 13,  True),
    ([5,3,6,2,4,6,7], 14,  False),
    ([5,3,6,2,4,6,7], 20,  False),
    ])

def test_two_sums(test_input, k, expected):
    root = listToTreeNode(test_input)
    assert Solution().findTarget(root, k) == expected
