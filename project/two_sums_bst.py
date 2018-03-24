
"""
Given a BST, find whether or not there are 2 numbers that add up to k
"""

import json
from project.treenode import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        bfs, values = [root], set()
        for node in bfs:
            if k - node.val in values: return True
            values.add(node.val)
            if node.left: bfs.append(node.left)
            if node.right: bfs.append(node.right)
        return False

def stringToTreeNode(input):
    if not input: return None

    input_values = json.loads(input)
    return listToTreeNode(input_values)

def listToTreeNode(input_values):
    if None in input_values: raise AttributeError("Invalid value None in list")

    root = TreeNode(int(input_values[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input_values):
        node = nodeQueue[front]
        front = front + 1

        item = input_values[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(input_values):
            break

        item = input_values[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            root = stringToTreeNode(line)
            line = lines.next()
            k = stringToInt(line)

            ret = Solution().findTarget(root, k)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
