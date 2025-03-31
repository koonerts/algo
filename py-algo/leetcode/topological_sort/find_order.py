"""
Find_order

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

    Given the number of tasks and a list of prerequisite pairs, write a method to
    find the ordering of tasks we should pick to finish all tasks.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
    before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]

    Example 2:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
    Output: []
    Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: [0 1 4 3 2 5]
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
"""

from collections import deque


def find_order(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

    Given the number of tasks and a list of prerequisite pairs, write a method to
    find the ordering of tasks we should pick to finish all tasks.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
    before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]

    Example 2:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
    Output: []
    Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: [0 1 4 3 2 5]
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
    """
    in_degrees_map = {i: 0 for i in range(tasks)}
    adjacency_map = {i: [] for i in range(tasks)}
    sorted_order = []
    q = deque()

    for pre_req, task in prerequisites:
        adjacency_map[pre_req].append(task)
        in_degrees_map[task] += 1

    for task, degree in in_degrees_map.items():
        if degree == 0:
            q.append(task)

    while q:
        for _ in range(len(q)):
            task = q.popleft()
            sorted_order.append(task)

            for child_task in adjacency_map[task]:
                in_degrees_map[child_task] -= 1
                if in_degrees_map[child_task] == 0:
                    q.append(child_task)

    return sorted_order if len(sorted_order) == tasks else []


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_order
    print(find_order([]))
