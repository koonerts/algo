"""
Symmetric

"""
def isSymmetric(root: TreeNode) -> bool:
        if not root: return True
def isMirror(n1: TreeNode, n2: TreeNode) -> bool:
            if not n1 and not n2:
                return True
            elif (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return False
            else:
                return isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)

        return isMirror(root.left, root.right)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isSymmetric
    print(isSymmetric([]))
