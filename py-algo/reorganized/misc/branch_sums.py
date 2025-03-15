"""
Sums

"""
def branchSums(root: BinaryTree):
    results = []
    if not root: return results
def recurse(node: BinaryTree, curr_sum=0):
        if not node:
            return
        else:
            if not node.left and not node.right:
                results.append(curr_sum + node.value)
            else:
                recurse(node.left, curr_sum + node.value)
                recurse(node.right, curr_sum + node.value)

    recurse(root)
    return results



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to branchSums
    print(branchSums([]))
