"""
Create_binary_tree_from_map

"""


def create_binary_tree_from_map(bt_map) -> BinaryTree:
    if "tree" in bt_map:
        tree = bt_map["tree"]
    else:
        tree = bt_map

    node_map = {}
    root: BinaryTree
    for n in tree["nodes"]:
        node_map[n["id"]] = BinaryTree(n["value"])
        if n["id"] == tree["root"]:
            root = node_map[n["id"]]

    for n in tree["nodes"]:
        node = node_map[n["id"]]

        if n["left"]:
            node.left = node_map[n["left"]]
            node.left.parent = node

        if n["right"]:
            node.right = node_map[n["right"]]
            node.right.parent = node

    return root


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to create_binary_tree_from_map
    print(create_binary_tree_from_map([]))
