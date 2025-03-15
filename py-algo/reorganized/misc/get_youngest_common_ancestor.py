"""
Youngest Common Ancestor

"""
def getYoungestCommonAncestor(topAncestor: AncestralTree, descendantOne: AncestralTree, descendantTwo: AncestralTree):
    d1_depth, d2_depth = 0, 0
    node1 = descendantOne
    while node1 != topAncestor:
        d1_depth += 1
        node1 = node1.ancestor

    node2 = descendantTwo
    while node2 != topAncestor:
        d2_depth += 1
        node2 = node2.ancestor

    depth_diff = abs(d1_depth-d2_depth)
    for _ in range(depth_diff):
        if d1_depth > d2_depth:
            descendantOne = descendantOne.ancestor
        else:
            descendantTwo = descendantTwo.ancestor

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    return descendantOne



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to getYoungestCommonAncestor
    print(getYoungestCommonAncestor([]))
