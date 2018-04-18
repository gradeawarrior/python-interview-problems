"""
Implement a min-heap, which is a binary tree such that:

- The data contained in each node is less than (or equal to) the data in that node's children
- The binary tree is complete

Note that you will need to implement an equivalent push() and pop() that will:

- Add some arbitrary number to the heap and rebalance
- pop() will always return and remove the smallest number, and rebalance the remaining heap
"""

from project.treenode import TreeNode
import project.config as config


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
                node.left = TreeNode(number, parent=node)
                break
            elif not node.right:
                node.right = TreeNode(number, parent=node)
                break
            full_tree.append(node.left)
            full_tree.append(node.right)
        return node

    def rebalance(self, node):
        top = node
        prev_child = None
        new_child = None
        while node:
            if new_child and prev_child:
                if   node.right and node.right.val == prev_child.val: node.right = new_child
                elif node.left  and node.left.val  == prev_child.val: node.left  = new_child
                prev_child = None
                new_child = None
            if config.debug:
                left = node.left.val if node.left else None
                right = node.right.val if node.right else None
                print("Current node: %s - left: %s - right: %s" % (node.val, left, right))

            if node.left and node.val > node.left.val:
                prev_child = node
                new_child = node.left
                node.left.parent = node.parent
                node.parent = node.left
                tleft = node.left.left
                tright = node.left.right
                node.left.left = node
                node.left.right = node.right
                node = node.left
                node.left.left = tleft
                node.left.right = tright
            if node.right and node.val > node.right.val:
                prev_child = node
                new_child = node.right
                node.right.parent = node.parent
                node.parent = node.right
                tleft = node.right.left
                tright = node.right.right
                node.right.left = node.left
                node.right.right = node
                node = node.right
                node.right.left = tleft
                node.right.right = tright

            if config.debug:
                left = node.left.val if node.left else None
                right = node.right.val if node.right else None
                print("Balanced node: %s - left: %s - right: %s" % (node.val, left, right))
            top = node.parent if node.parent else node
            node = node.parent

        if config.debug:
            left = top.left.val if top.left else None
            right = top.right.val if top.right else None
            print("top: %s - left: %s - right: %s" % (top.val, left, right))
        self.heap = top

    def to_list(self):
        if self.heap is None: return []
        ret = []
        full_tree = [self.heap]
        for node in full_tree:
            ret.append(node.val)
            if node.left: full_tree.append(node.left)
            if node.right: full_tree.append(node.right)
        return ret

