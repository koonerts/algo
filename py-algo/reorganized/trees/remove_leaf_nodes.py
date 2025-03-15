"""
Leaf Nodes

"""
def removeLeafNodes(root: TreeNode, target: int) -> TreeNode:
        if not root or (not root.left and not root.right and root.val == target): return None
def remove(node: TreeNode, parent: TreeNode, rel: RelationshipToParent):
            if not node:
                return
            else:
                remove(node.left, node, RelationshipToParent.LEFT)
                remove(node.right, node, RelationshipToParent.RIGHT)

                if node.val == target and not node.left and not node.right:
                    if rel == RelationshipToParent.LEFT:
                        parent.left = None
                    else:
                        parent.right = None
        remove(root, None, None)

        if (not root.left and not root.right and root.val == target):
            return None
        else:
            return root


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to removeLeafNodes
    print(removeLeafNodes([]))
