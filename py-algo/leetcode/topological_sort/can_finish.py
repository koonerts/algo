"""
Finish

"""

from collections import deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    in_degree_map = {i: 0 for i in range(numCourses)}
    adj_graph = {i: [] for i in range(numCourses)}

    for parent, child in prerequisites:
        in_degree_map[child] += 1
        adj_graph[parent].append(child)

    q = deque()
    for course, in_degree in in_degree_map.items():
        if in_degree == 0:
            q.append(course)

    cnt = 0
    while q:
        parent_course = q.popleft()
        cnt += 1

        for child_course in adj_graph[parent_course]:
            in_degree_map[child_course] -= 1
            if in_degree_map[child_course] == 0:
                q.append(child_course)
    return cnt >= numCourses


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to canFinish
    print(canFinish([]))
