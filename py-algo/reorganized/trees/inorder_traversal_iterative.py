"""
Traversal_iterative

"""
def inorderTraversal_iterative(root: TreeNode) -> list[int]:
        result = []
        stack = [root]

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to inorderTraversal_iterative
    print(inorderTraversal_iterative([]))
