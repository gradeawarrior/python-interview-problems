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

import config as config
from project.treenode import debug_node


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        elif not root.left and not root.right: return 1
        depth = 1
        current_d = [root]
        next_d = []
        while len(current_d) > 0:
            if config.debug: debug_node(current_d[0])
            if current_d[0].left: next_d.append(current_d[0].left)
            if current_d[0].right: next_d.append(current_d[0].right)
            current_d.pop(0)
            if not current_d:
                if next_d: depth += 1
                current_d = next_d
                next_d = []
        return depth

