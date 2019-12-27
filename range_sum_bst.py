class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def range_sum_bst(root: TreeNode, L: int, R: int) -> int:
    node_queue = [root]
    upperbound = R
    lowerbound = L
    bst_sum = 0
    while len(node_queue) > 0:
        curr_node = node_queue.pop()
        if curr_node.val >= L and curr_node.val <= R:
            bst_sum+=curr_node.val

        if curr_node.left is not None:
            node_queue.append(curr_node.left)
        if curr_node.right is not None: 
            node_queue.append(curr_node.right)

    return bst_sum        