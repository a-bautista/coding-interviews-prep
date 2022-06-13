class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def solve(self, root):
        def dfs_recursive(root, c_path):
            if root:
                c_path += str(root.val)
                if not root.left and not root.right:
                    paths.append(c_path)
                else:
                    c_path += '->'
                    dfs_recursive(root.left, c_path)
                    dfs_recursive(root.right, c_path)


        paths = []
        dfs_recursive(root, '')
        return paths


def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    solution = Solution()
    res = solution.solve(root)
    #res = dfs_recursive(root)
    print(res)

main()