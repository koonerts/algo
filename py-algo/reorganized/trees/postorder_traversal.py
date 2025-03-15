"""
Traversal

"""
def postorderTraversal(root: TreeNode) -> list[int]:
        out = []
        if root:
            out += self.postorderTraversal(root.left)
            out += self.postorderTraversal(root.right)
            out.append(root.val)
        else:
            out.append(None)
        return out


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to postorderTraversal
    print(postorderTraversal([]))
