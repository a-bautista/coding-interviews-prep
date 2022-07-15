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

    The diameter of the tree is the height of the left node + the height of the right node.


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        # trick to keep the variable global res = [0]
        # res = [0]
        def dfs(root):
            if not root:
                # by definition, a None node has a height of -1
                return -1

            left = dfs(root.left)
            
            right = dfs(root.right)
            
            # diameter is equal to the height of the left and right nodes + 2 
            # (2 is for balancing) the nodes in case we have None values
            self.diameter = max(self.diameter, 2 + left + right)

            # return the height 
            # 1 is for balancing the math when you reach the bottom of the tree
            # the bottom is 0, so when going up in the recursion, you will have 1
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter

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
