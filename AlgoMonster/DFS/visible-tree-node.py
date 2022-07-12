class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
# class Solution:
#     def helper(self, root: Node) -> int:        
#         main_val = root.val
#         global res
#         res = 0
#         if root:
#             sol = self.visible_tree_node(root, main_val, res)
#         return sol
    
#     # In recursion, the values are not saved    
#     def visible_tree_node(self, root: Node, main_val: int, res: int) -> int:
#         if root:
#             if root.val>=main_val:
#                 res +=1
#                 self.visible_tree_node(root.left, main_val, res)
#                 self.visible_tree_node(root.right, main_val, res)
#         return res


def visible_tree_node(root: Node) -> int:
    def dfs(root: Node, res: int) -> int:
        
        if not root:
            return 0

        
        total = 0
        if root.val>=res:
            total+=1

        # The totals need to be added, so they can be carried out in the next levels of recursion
        total+=dfs(root.left, max(res, root.val))
        total+=dfs(root.right, max(res, root.val))

        return total

    return dfs(root, float('-inf'))
    
def main():

    node = Node(5)
    node.left = Node(4)
    node.right = Node(6)
    node.left.left = Node(3)
    node.left.right = Node(8)
    node.right = Node(6)

    sol = visible_tree_node(node)
    print(sol)
    # res = sol.helper(node)
    # print(res)

main()