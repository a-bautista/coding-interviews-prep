class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs_iterative(root):
    stack = []
    res   = []
    stack.append((root, str(root.val)))

    while stack:
        current_node, path = stack.pop()

        # if you have reached the deepest leaf without any child, then attach the current path which contains the results
        if not current_node.left and not current_node.right:
            res.append(path)

        if current_node.left:
            stack.append((current_node.left, path + '->' + str(current_node.left.val)))

        if current_node.right:
            stack.append((current_node.right, path + '->' + str(current_node.right.val)))

    return res

def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    res = dfs_iterative(root)
    print(res)

main()