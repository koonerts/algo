"""
Create_bst_from_map

"""


def create_bst_from_map(bst_map) -> BST:
    if "tree" in bst_map:
        tree = bst_map["tree"]
    else:
        tree = bst_map

    node_map = {}
    root: BST
    for n in tree["nodes"]:
        node_map[n["id"]] = BST(n["value"])
        if n["id"] == tree["root"]:
            root = node_map[n["id"]]

    for n in tree["nodes"]:
        node = node_map[n["id"]]
        if n["left"]:
            node.left = node_map[n["left"]]
        if n["right"]:
            node.right = node_map[n["right"]]
    return root


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to create_bst_from_map
    print(create_bst_from_map([]))
