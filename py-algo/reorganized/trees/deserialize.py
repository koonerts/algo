"""
Deserialize

Decodes your encoded data to tree.
"""


def deserialize(data: str) -> TreeNode:
    """
    Decodes your encoded data to tree.
    """
    map = json.loads(data)
    return self.buildTree_Pre(map.inorder, map.preorder)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to deserialize
    print(deserialize([]))
