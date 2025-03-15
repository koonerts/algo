"""
Binary Tree

"""
def invertBinaryTree(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    return tree



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to invertBinaryTree
    print(invertBinaryTree([]))
