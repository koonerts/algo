"""
Tree_ Post

Given inorder and postorder traversal of a tree, construct the binary tree.
        Note: You may assume that duplicates do not exist in the tree.

        Ex:
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        Return the following binary tree:
            3
           /           9  20
            /             15   7
"""
def buildTree_Post(inorder: list[int], postorder: list[int]) -> TreeNode:
        """
        Given inorder and postorder traversal of a tree, construct the binary tree.
        Note: You may assume that duplicates do not exist in the tree.

        Ex:
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        Return the following binary tree:
            3
           / \
          9  20
            /  \
           15   7
        """
def build(bound=None):
            if not inorder or inorder[-1] == bound:
                return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(bound)
            return root

        return build()


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to buildTree_Post
    print(buildTree_Post([]))
