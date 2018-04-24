"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

return its depth = 3.
"""

import pytest
import time
from project.treenode import TreeNode, convert_list_to_tree
from project.max_depth_btree import Solution


@pytest.mark.parametrize("test_input, expected", [
    ([3,9,20,None,None,15,7], 3),
    ([1], 1),
    ([1,2], 2),
    ([1,2,3], 2),
    ([1,None,2], 2),
    ([1,2,3,4], 3),
    ])

def test_max_subarray_optimized(test_input, expected):
    btree = convert_list_to_tree(test_input)
    assert Solution().maxDepth(btree) == expected

