"""
Tree Diameter

"""
def binaryTreeDiameter(tree):
    if not tree: return 0
def find_depths(node):
        nonlocal max_diameter
        if not node:
            return 0
        else:
            left_depth = find_depths(node.left)
            right_depth = find_depths(node.right)
            max_diameter = max(max_diameter, left_depth+right_depth)
            return max(left_depth, right_depth) + 1
    max_diameter = 0
    find_depths(tree)
    return max_diameter


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to binaryTreeDiameter
    print(binaryTreeDiameter([]))
