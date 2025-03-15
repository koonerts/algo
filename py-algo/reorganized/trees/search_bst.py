"""
B S T

"""
def searchBST(root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to searchBST
    print(searchBST([]))
