"""
Into B S T

"""
def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)

        node = root
        while node:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        return root


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to insertIntoBST
    print(insertIntoBST([]))
