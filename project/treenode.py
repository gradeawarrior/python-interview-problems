
"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def to_list(self):
        ret = []
        full_tree = [self]
        for node in full_tree:
            ret.append(node.val)
            if node.left: full_tree.append(node.left)
            if node.right: full_tree.append(node.right)
        return ret

