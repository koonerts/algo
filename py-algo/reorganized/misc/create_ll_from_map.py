"""
Create_ll_from_map

"""


def create_ll_from_map(nmap) -> LinkedList:
    head = None
    node_map = {}
    nmap = nmap.get("linkedList", nmap)
    for n in nmap["nodes"]:
        node = LinkedList(n["value"])
        node_map[n["id"]] = node
        if n["id"] == nmap["head"]:
            head = node

    for n in nmap["nodes"]:
        if n["next"] is not None:
            node = node_map[n["id"]]
            node.next = node_map[n["next"]]
    return head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to create_ll_from_map
    print(create_ll_from_map([]))
