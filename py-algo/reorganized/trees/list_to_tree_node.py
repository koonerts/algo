"""
To Tree Node

"""
def listToTreeNode(nums) -> TreeNode:
    node_map = {}
    for i, num in enumerate(nums):
        if num is None:
            node_map[i] = None
        else:
            node = TreeNode(num)
            node_map[i] = node

    for i, num in enumerate(nums):
        left = 2*i + 1
        right = left + 1
        if left < len(nums) and left in node_map:
            node_map[i].left = node_map[left]
        if right < len(nums) and right in node_map:
            node_map[i].right = node_map[right]
    return node_map[0]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to listToTreeNode
    print(listToTreeNode([]))
