"""
Bipartite

"""

from collections import deque


def isBipartite(graph: list[list[int]]) -> bool:
    if not graph:
        return True
    s1, s2 = set(), set()

    set_number = 1
    q = deque([0])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if set_number == 1:
                s1.add(node)
            else:
                s2.add(node)

            for child in graph[node]:
                if child not in s1 and child not in s2:
                    q.append(child)
        set_number *= -1
    print(s1)
    print(s2)
    return s1.isdisjoint(s2)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isBipartite
    print(isBipartite([]))
