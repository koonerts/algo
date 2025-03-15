"""
Order

"""


from collections import deque
def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if not prerequisites: return list(range(numCourses))

        in_degree, graph = {i:0 for i in range(numCourses)}, {i:[] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            in_degree[course] += 1
            graph[pre_req].append(course)
            if pre_req not in in_degree:
                in_degree[pre_req] = 0

        q = deque()
        for c in (c for c in in_degree if in_degree[c] == 0):
            q.append(c)

        result = []
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                result.append(course)
                for child in graph[course]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        q.append(child)
        return result if len(result) == numCourses else []


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findOrder
    print(findOrder([]))
