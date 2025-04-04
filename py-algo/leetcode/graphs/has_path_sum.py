"""
Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
        Note: A leaf is a node with no children.

        Example: Given the below binary tree and sum = 22,
              5
             /             4   8
           /   /           11  13  4
         /  \              7    2      1
        return true, as there exist a root-to-leaf path 5->4->11->2 which sums to 22
"""


def hasPathSum(root: TreeNode, sum: int) -> bool:
    """
        Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
        Note: A leaf is a node with no children.

        Example: Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        return true, as there exist a root-to-leaf path 5->4->11->2 which sums to 22
        """
    if not root:
        return False

    sum -= root.val
    if not root.left and not root.right:
        return sum == 0

    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to hasPathSum
    print(hasPathSum([]))
