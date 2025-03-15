"""
Bst

"""
def validateBst(tree: BST, low_limit=float('-inf'), high_limit=float('inf')):
    if not tree:
        return True
    else:
        return low_limit <= tree.value < high_limit \
               and validateBst(tree.left, low_limit, tree.value) \
               and validateBst(tree.right, tree.value, high_limit)



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to validateBst
    print(validateBst([]))
