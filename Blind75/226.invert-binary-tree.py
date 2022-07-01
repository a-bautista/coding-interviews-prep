'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Normal
         4
        / \
       2   7
      / \ / \
     1  3 6  9

Inverted

         4
        / \
       7   2
      / \ / \
     9  6 3  1@

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque
def invert_binary_tree_level_bfs(root):
    '''
        Solved by using BFS level by level approach. Not the best one because you consume 
        more memory due to the list for storing the results.
    '''

    if not root:
        return []

    res = []
    queue = deque()
    queue.appendleft(root)
    
    res.append(root.val)

    while queue:

        size = len(queue)
        for _ in range(size):
            current_node = queue.popleft()

            if current_node.right:
                res.append(current_node.right.val)
                queue.appendleft(current_node.right)
            if current_node.left:
                res.append(current_node.left.val)
                queue.appendleft(current_node.left)
    return res

def invert_binary_tree_bfs(root):

    if not root:
        return None

    queue = deque([root])

    while queue:

        current_node = queue.popleft()

        # invert the binary nodes
        current_node.left, current_node.right = current_node.right, current_node.left

        # append the nodes by the right side of the queue
        if current_node.left:    
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return root

def main():
    node = Node(4)
    node.left = Node(2)
    node.right = Node(7)
    node.left.left = Node(1)
    node.left.right = Node(3)
    node.right.left = Node(6)
    node.right.right = Node(9)
    res = invert_binary_tree_bfs(node)
    print(res)

main()