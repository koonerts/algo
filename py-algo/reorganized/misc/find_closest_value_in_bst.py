"""
Closest Value In Bst

"""


def findClosestValueInBst(tree: BST, target: int):
    node = tree
    closest_val = node.value
    while node:
        if node.value == target:
            return node.value
        elif node.value > target:
            node = node.left
        else:
            node = node.right

        if abs(node.value - target) < abs(closest_val - target):
            closest_val = node.value
    return closest_val


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findClosestValueInBst
    print(findClosestValueInBst([]))
