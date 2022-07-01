# 235. Lowest Common Ancestor of a Binary Search Tree
# Easy

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node 
# in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solve_lca(root, p, q):
    lca = None
    def recurse_tree(root, p, q):
        nonlocal lca

        # if you hit the end of the tree then return None
        if not root:
            return None

        left = recurse_tree(root.left, p, q)
        right = recurse_tree(root.right, p, q)

        # If you find one of the targets in the middle then assign the value to True
        mid = root.val == p or root.val == q

        # if either the left, middle or right node were True which means the 
        # lca was found then assign lca
        if mid + left + right >=2:
            lca = root.val

        # return either True or False based on the 3 conditions
        return mid or left or right

    recurse_tree(root, p, q)
    return lca

def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    p = 10 
    q = 12
    res = solve_lca(root, p, q)
    print(res)

main()