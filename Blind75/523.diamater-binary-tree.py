'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

             1
            / \
           2   3
          / \
         4   5         

Input: root = [1,2,3,4,5]
Output: 3 because of the edges
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    # def __init__(self):
    #     self.treeDiameter = 0

    # def find_diameter(self, root):
    #     self.diameterBinaryTree(root)
    #     return self.treeDiameter

    # def diameterBinaryTree(self, root):
    #     if not root:
    #         return 0

    #     L = self.diameterBinaryTree(root.left)
    #     R = self.diameterBinaryTree(root.right)

    #     diameter = L + R + 1 # 1 indicates to count when the edge when the nodes have reached 0

    #     self.treeDiameter = max(diameter, self.treeDiameter)

    #     # height
    #     return max(L, R) + 1

    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            # height
            return 1 + max(left, right)
        dfs(root)
        return res[0]


def main():
    treeDiameter = TreeDiameter()
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(6)
    # print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.diameterOfBinaryTree(root)))

main()
