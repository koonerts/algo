"""
Recurse

"""
def recurse(root: TreeNode, out, traversal_type: TraversalType):
        if root is None:
            return

        if traversal_type == TraversalType.PREORDER:
            out.append(root.val)
            self.recurse(root.left, out, traversal_type)
            self.recurse(root.right, out, traversal_type)
        elif traversal_type == TraversalType.INORDER:
            self.recurse(root.left, out, traversal_type)
            out.append(root.val)
            self.recurse(root.right, out, traversal_type)
        elif traversal_type == TraversalType.POSTORDER:
            self.recurse(root.left, out, traversal_type)
            self.recurse(root.right, out, traversal_type)
            out.append(root.val)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to recurse
    print(recurse([]))
