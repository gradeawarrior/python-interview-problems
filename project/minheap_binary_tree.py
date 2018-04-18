"""
Implement a min-heap, which is a binary tree such that:

- The data contained in each node is less than (or equal to) the data in that node's children
- The binary tree is complete

Note that you will need to implement an equivalent push() and pop() that will:

- Add some arbitrary number to the heap and rebalance
- pop() will always return and remove the smallest number, and rebalance the remaining heap
"""

from project.treenode import TreeNode


class Heap:
    def __init__(self, num_list = []):
        self.heap = None
        node = self.heap
        for number in num_list:
            self.insert_into_tree(number)

    def insert_into_tree(self, number):
        if self.heap is None:
            self.heap = TreeNode(number)
            return self.heap
        full_tree = [self.heap]

        for node in full_tree:
            if not node.left:
                node.left = TreeNode(number)
                break
            elif not node.right:
                node.right = TreeNode(number)
                break
            full_tree.append(node.left)
            full_tree.append(node.right)
        return node

    def to_list(self):
        if self.heap is None: return []
        ret = []
        full_tree = [self.heap]
        for node in full_tree:
            ret.append(node.val)
            if node.left: full_tree.append(node.left)
            if node.right: full_tree.append(node.right)
        return ret

