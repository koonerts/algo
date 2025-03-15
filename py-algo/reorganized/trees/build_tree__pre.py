"""
Tree_ Pre

Given inorder and postorder traversal of a tree, construct the binary tree.
        Note: You may assume that duplicates do not exist in the tree.

        Ex:
        inorder = [9,3,15,20,7]
        preorder = [3,9,20,15,7]
        Return the following binary tree:
            3
           /           9  20
            /             15   7
"""
def buildTree_Pre(inorder: list[int], preorder: list[int]) -> TreeNode:
        """
        Given inorder and postorder traversal of a tree, construct the binary tree.
        Note: You may assume that duplicates do not exist in the tree.

        Ex:
        inorder = [9,3,15,20,7]
        preorder = [3,9,20,15,7]
        Return the following binary tree:
            3
           / \
          9  20
            /  \
           15   7
        """
def build(bound=None):
            if not inorder or inorder[0] == bound:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = build(root.val)
            inorder.pop(0)
            root.right = build(bound)
            return root

        return build()


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to buildTree_Pre
    print(buildTree_Pre([]))
