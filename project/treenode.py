
"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class TreeNode(object):
    def __init__(self, x, parent=None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = parent

    def to_list(self):
        ret = []
        full_tree = [self]
        for node in full_tree:
            ret.append(node.val)
            if node.left: full_tree.append(node.left)
            if node.right: full_tree.append(node.right)
        return ret

def convert_list_to_tree(A):
    """
    Convenience function that converts a list to a BinaryTree. Note that this is
    **not** a full tree, and thus handles insertion of null's to create different
    tree structures.

    Example:

    Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
    """
    root = TreeNode(A[0])
    btree = [root]
    idx = 1
    while idx < len(A):
        num1 = A[idx]
        num2 = A[idx+1] if idx+1 < len(A) else None
        if btree:
            if num1 is not None:
                node = TreeNode(num1, parent=btree[0])
                btree[0].left = node
                btree.append(node)
            if num2 is not None:
                node = TreeNode(num2, parent=btree[0])
                btree[0].right = node
                btree.append(node)
            btree.pop(0)
        idx += 2
    return root

def debug_node(node, msg=""):
    """
    Convenience function that prints the current node value, as well as the left and right value
    """
    if not node: return
    left = node.left.val if node.left else None
    right = node.right.val if node.right else None
    msg = "%s - " % msg if msg else ""
    msg += "val: %s - left: %s - right: %s" % (node.val, left, right)
    print(msg)
