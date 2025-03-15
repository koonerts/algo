"""
In Graph

"""


from collections import deque
def cycleInGraph(edges):
    in_degrees = {i:0 for i in range(len(edges))}
    for node, children in enumerate(edges):
        for child in children:
            in_degrees[child] += 1

    q = deque()
    for node in in_degrees:
        if in_degrees[node] == 0:
            q.append(node)

    node_cnt = 0
    while q:
        node = q.popleft()
        node_cnt += 1

        for child in edges[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                q.append(child)
    return True if node_cnt != len(edges) else False



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to cycleInGraph
    print(cycleInGraph([]))
