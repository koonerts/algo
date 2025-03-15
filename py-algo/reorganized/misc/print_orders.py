"""
Print_orders

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: There is only possible ordering of the tasks.

    Example 2:
    Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
    Output:
    1) [3, 2, 0, 1]
    2) [3, 2, 1, 0]
    Explanation: There are two possible orderings of the tasks meeting all prerequisites.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output:
    1) [0, 1, 4, 3, 2, 5]
    2) [0, 1, 3, 4, 2, 5]
    3) [0, 1, 3, 2, 4, 5]
    4) [0, 1, 3, 2, 5, 4]
    5) [1, 0, 3, 4, 2, 5]
    6) [1, 0, 3, 2, 4, 5]
    7) [1, 0, 3, 2, 5, 4]
    8) [1, 0, 4, 3, 2, 5]
    9) [1, 3, 0, 2, 4, 5]
    10) [1, 3, 0, 2, 5, 4]
    11) [1, 3, 0, 4, 2, 5]
    12) [1, 3, 2, 0, 5, 4]
    13) [1, 3, 2, 0, 4, 5]
"""


from collections import deque
def print_orders(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: There is only possible ordering of the tasks.

    Example 2:
    Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
    Output:
    1) [3, 2, 0, 1]
    2) [3, 2, 1, 0]
    Explanation: There are two possible orderings of the tasks meeting all prerequisites.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output:
    1) [0, 1, 4, 3, 2, 5]
    2) [0, 1, 3, 4, 2, 5]
    3) [0, 1, 3, 2, 4, 5]
    4) [0, 1, 3, 2, 5, 4]
    5) [1, 0, 3, 4, 2, 5]
    6) [1, 0, 3, 2, 4, 5]
    7) [1, 0, 3, 2, 5, 4]
    8) [1, 0, 4, 3, 2, 5]
    9) [1, 3, 0, 2, 4, 5]
    10) [1, 3, 0, 2, 5, 4]
    11) [1, 3, 0, 4, 2, 5]
    12) [1, 3, 2, 0, 5, 4]
    13) [1, 3, 2, 0, 4, 5]
    """
    in_degrees_map = {i:0 for i in range(tasks)}
    adjacency_map = {i:[] for i in range(tasks)}
    sorted_orders = deque([[]])
    sources = deque()

    for parent_task, child_task in prerequisites:
        adjacency_map[parent_task].append(child_task)
        in_degrees_map[child_task] += 1

    for task, degree in in_degrees_map.items():
        if degree == 0: sources.append(task)

    while sources:
        level_orders = []
        for _ in range(len(sources)):
            task = sources.popleft()

            for child_task in adjacency_map[task]:
                in_degrees_map[child_task] -= 1
                if in_degrees_map[child_task] == 0:
                    sources.append(child_task)

    # TODO: Come back to

    for order in sorted_orders:
        print(order)



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to print_orders
    print(print_orders([]))
