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
        self.last_leaf = None
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
                self.last_leaf = node.left
                break
            elif not node.right:
                node.right = TreeNode(number, parent=node)
                self.last_leaf = node.right
                break
            full_tree.append(node.left)
            full_tree.append(node.right)
        return node

    def rebalance(self, node):
        if config.debug: self.debug_node(node, msg="Current node")

        if node.left and node.val > node.left.val:
            # Reset parent pointers
            node.left.parent = node.parent
            node.parent = node.left
            if node.left.parent and node.left.parent.left.val == node.val:
                node.left.parent.left = node.left
            elif node.left.parent:
                node.left.parent.right = node.left

            # Reset left and right pointers
            tleft = node.left.left
            tright = node.left.right
            node.left.left = node
            node.left.right = node.right
            node = node.left
            node.left.left = tleft
            node.left.right = tright
        if node.right and node.val > node.right.val:
            # Reset parent pointers
            node.right.parent = node.parent
            node.parent = node.right
            if node.right.parent and node.right.parent.left.val == node.val:
                node.right.parent.left = node.right
            elif node.right.parent:
                node.right.parent.right = node.right

            # Reset left and right pointers
            tleft = node.right.left
            tright = node.right.right
            node.right.left = node.left
            node.right.right = node
            node = node.right
            node.right.left = tleft
            node.right.right = tright

        if config.debug: self.debug_node(node, msg="Balanced node")
        return node

    def rebalance_recursive(self, node):
        top = node
        while node:
            node = self.rebalance(node)
            top = node.parent if node.parent else node
            node = node.parent

        if config.debug: self.debug_node(node, msg="Root")
        self.heap = top

    def push(self, number):
        node = self.insert_into_tree(number)
        self.rebalance_recursive(node)

    def pop(self):
        # Handle situation where the heap is empty
        if not self.heap: return None
        ret = self.heap.val

        # Handle situation where the heap is only of size 1 or 2
        if not self.heap.left and not self.heap.right:
            self.heap = None
            return ret
        elif not self.heap.right:
            self.heap = self.heap.left
            self.heap.parent = None
            return ret

        # Shift Tree
        if config.debug: self.debug_node(self.last_leaf, msg="Leaf")
        new_root = self.last_leaf
        if new_root.parent.left.val == new_root.val:
            new_root.parent.left = None
        else:
            new_root.parent.right = None
        new_root.parent = None
        new_root.left = self.heap.left
        new_root.right = self.heap.right
        self.heap.left.parent = new_root
        self.heap.right.parent = new_root

        node = new_root
        update_root = True
        while node.left:
            if not node.right and node.val > node.left.val:
                node = self.rebalance(node)
                node = node.left
            elif node.right and node.left.val < node.right.val:
                node = self.rebalance(node)
                node = node.left
            elif node.right and node.right.val <= node.left.val:
                node = self.rebalance(node)
                node = node.right
            else:
                raise RuntimeError("Program should never hit this")
            if update_root:
                new_root = node.parent
                update_root = False

        self.heap = new_root
        return ret

    def to_list(self):
        if self.heap is None: return []
        ret = []
        full_tree = [self.heap]
        for node in full_tree:
            ret.append(node.val)
            if node.left: full_tree.append(node.left)
            if node.right: full_tree.append(node.right)
        return ret

    def get_last_leaf(self):
        if self.heap is None:
            self.last_leaf = None
            return None
        full_tree = [self.heap]
        for node in full_tree:
            ret.append(node.val)
            if node.left: self.last_leaf
            if node.right: self.last_leaf
        return self.last_leaf

    def debug_node(self, node, msg=""):
        if not node: return
        left = node.left.val if node.left else None
        right = node.right.val if node.right else None
        msg = "%s - " % msg if msg else ""
        msg += "val: %s - left: %s - right: %s" % (node.val, left, right)
        print(msg)

