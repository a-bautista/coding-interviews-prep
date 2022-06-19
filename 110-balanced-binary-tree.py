'''
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as:

    A binary tree in which the left and right subtrees of every node differ in height by no more than 1.

    Example 1:

        3
       / \
      9   20
          / \
         15  7     

    Input: root = [3,9,20,null,null,15,7]
    Output: true

            1
           / \
          2   2
         / \
        3   3
       / \
      4   4  

    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

    Input: root = []
    Output: true
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        # edge case
        if root is None:
            return True
        self.ans = True

        def recursion(root):
            if root is None:
                return 0
            # similar to the tree lca
            left = recursion(root.left)
            right = recursion(root.right)
            # why this?
            if abs(left - right)>1:
                return False
            # why this?
            return 1 + max(left, right)
        recursion(root)
        return self.ans
