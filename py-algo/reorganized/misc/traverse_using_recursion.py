"""
Traverse_using_recursion

"""
def traverse_using_recursion(root: TreeNode) -> list[list[int]]:
    result = []
    if not root: return result
def level_order_traverse(node: TreeNode, level: int):
        if node:
            if len(result) < level:
                result.append([node.val])
            else:
                result[level-1].append(node.val)

            level_order_traverse(node.left, level+1)
            level_order_traverse(node.right, level+1)

    level_order_traverse(root, 1)
    return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to traverse_using_recursion
    print(traverse_using_recursion([]))
