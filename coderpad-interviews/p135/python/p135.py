class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def min_path_sum(node: Node):
    mn, path = int(1e9), []

    def dfs(node: Node, sum_, path_):
        path_.append(node)
        global mn, path
        if node.left == None and node.right == None:
            if sum_ < mn:
                mn, path = sum_, path_
                return

        if node.left != None:
            dfs(node.left, sum_ + node.item, path_)

        if node.right != None:
            dfs(node.right, sum_ + node.item, path_)

    dfs(node)

    return mn
