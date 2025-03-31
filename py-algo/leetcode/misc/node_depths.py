"""
Depths

"""
def nodeDepths(root: BinaryTree):
def sum_depths(node: BinaryTree, level=0):
        nonlocal depth_sum
        if not node:
            return
        else:
            depth_sum += level
            sum_depths(node.left, level+1)
            sum_depths(node.right, level+1)
    depth_sum = 0
    sum_depths(root)
    return depth_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to nodeDepths
    print(nodeDepths([]))
