"""
In Order Traversal

"""


def iterativeInOrderTraversal(tree, callback):
    node = tree
    while node.parent:
        node = node.parent

    prev = None
    while node:
        if node.left and prev != node.left:
            prev = node
            node = node.left
        else:
            callback(node)
            if node.right:
                prev = node
                node = node.right
            else:
                while node.parent and node.parent.right == node:
                    node = node.parent

                prev = node
                node = node.parent


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to iterativeInOrderTraversal
    print(iterativeInOrderTraversal([]))
