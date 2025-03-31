"""
Topological_sort

Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its
    vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

    Given a directed graph, find the topological ordering of its vertices.

    Example 1:
    Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
    Output: Following are the two valid topological sorts for the given graph:
    1) 3, 2, 0, 1
    2) 3, 2, 1, 0
"""

from collections import deque


def topological_sort(vertices, edges):
    """
    Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its
    vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

    Given a directed graph, find the topological ordering of its vertices.

    Example 1:
    Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
    Output: Following are the two valid topological sorts for the given graph:
    1) 3, 2, 0, 1
    2) 3, 2, 1, 0
    """
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph
    q = deque()

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    for node, cnt in in_degree.items():
        if cnt == 0:
            q.append(node)

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            sortedOrder.append(node)

            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)

    return sortedOrder


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to topological_sort
    print(topological_sort([]))
