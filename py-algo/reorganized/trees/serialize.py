"""
Serialize

Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
"""


def serialize(root: TreeNode) -> str:
    """
    Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    inorder = self.inorderTraversal(root)
    preorder = self.preorderTraversal(root)
    return json.dumps({"inorder": inorder, "preorder": preorder})


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to serialize
    print(serialize([]))
