"""
Implement a min-heap, which is a binary tree such that:

- The data contained in each node is less than (or equal to) the data in that node's children
- The binary tree is complete

Note that you will need to implement an equivalent push() and pop() that will:

- Add some arbitrary number to the heap and rebalance
- pop() will always return and remove the smallest number, and rebalance the remaining heap
"""

import pytest
from project.minheap_binary_tree import Heap


@pytest.mark.parametrize("test_input", [
    ([]),
    ([2, 3, 4]),
    ([2, 3, 4, 5, 6]),
    ([2, 4, 6, 8, 10]),
    ])

def test_create_full_binary_tree(test_input):
    """
    Test that my logic for creating a heap from a sorted List is correct
    """
    heap = Heap(test_input)
    actual = heap.to_list()
    assert isinstance(actual, list)
    assert actual == test_input

@pytest.mark.parametrize("test_input, number, expected_stree, expected", [
    ([], 1, [1], [1]),
    ([2, 3, 4], 1, [3, 1], [2, 3, 4, 1]),
    ([2, 3, 4, 5, 6], 1, [4, 1], [2, 3, 4, 5, 6, 1]),
    ([2, 4, 6, 8, 10], 1, [6, 1], [2, 4, 6, 8, 10, 1]),
    ])

def test_insert_number_into_tree(test_input, number, expected_stree, expected):
    """
    Test that my logic for Heap.insert_into_tree() is working as prescribed
    """
    heap = Heap(test_input)

    # Ensure that subtree returned from calling Heap.insert_into_tree() is expected
    subtree = heap.insert_into_tree(number)
    actual_stree = subtree.to_list()
    assert isinstance(actual_stree, list)
    assert actual_stree == expected_stree

    # Ensure that entire tree is correct and complete
    actual = heap.to_list()
    assert isinstance(actual, list)
    assert actual == expected

@pytest.mark.parametrize("test_input, number, expected", [
    ([], 1, [1]),
    ([2, 3, 4], 1, [1, 2, 4, 3]),
    ([2, 3, 4, 5, 6], 1, [1, 3, 2, 5, 6, 4]),
    ([2, 4, 6, 8, 10], 1, [1, 4, 2, 8, 10, 6]),
    ([2, 4, 6, 8, 10], 5, [2, 4, 5, 8, 10, 6]),
    ([2, 4, 6, 8, 10], 7, [2, 4, 6, 8, 10, 7]),
    ])

def test_rebalance_tree(test_input, number, expected):
    """
    Test that my logic for Heap.rebalance() is working as prescribed
    """
    heap = Heap(test_input)

    # Ensure that subtree returned from calling Heap.insert_into_tree() is expected
    subtree = heap.insert_into_tree(number)
    heap.rebalance(subtree)

    # Ensure that entire tree is correct and complete
    actual = heap.to_list()
    assert isinstance(actual, list)
    assert actual == expected
