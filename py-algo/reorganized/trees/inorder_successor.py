"""
Successor

"""
def inorderSuccessor(root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        while root:
            if root.val == p.val:
                if root.right:
                    successor = root.right
                    while successor and successor.left:
                        successor = successor.left
                    return successor
                else:
                    return successor
            elif root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to inorderSuccessor
    print(inorderSuccessor([]))
