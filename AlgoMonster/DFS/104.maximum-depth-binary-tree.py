'''
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the 
    longest path from the root node down to the farthest leaf node.
    Find the max depth of a binary tree. 

            1
           / \
          2   3 
         / \
        4   5   <-- max depth = 3 

            1
           / \
          2   3 
         / \   \
        4   5  10 
       /
      12         <-- max depth = 4
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SolutionDFS:
    def maxDepth(self, root):    
        return self.dfs(root, 0)

    def dfs(self, root, depth):
        if not root:
            return depth
        return max(self.dfs(root.left, depth + 1), self.dfs(root.right, depth + 1))

    
def main():

    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.right = Node(7)
    sol = SolutionDFS()
    res = sol.maxDepth(root)
    print(res)


main()
