from collections import deque
class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

def bfs(root, target):
    queue = deque(root)
    while queue:
        current_node = queue.popleft()
        size = len(current_node)
        for _ in range(size):
            if current_node == target:
                return current_node.key
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return -1
