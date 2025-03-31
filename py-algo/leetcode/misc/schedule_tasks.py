"""
Schedule_tasks

You are given a list of tasks that need to be run, in any order, on a server.
    Each task will take one CPU interval to execute but once a task has finished, it has a cooling period
    during which it can’t be run again.

    If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that
    the server needs to finish all tasks. If at any time the server can’t execute any task then it must stay idle.

    Example 1:
    Input: [a, a, a, b, c, c], K=2
    Output: 7
    Explanation: a -> c -> b -> a -> c -> idle -> a

    Example 2:
    Input: [a, b, a], K=3
    Output: 5
    Explanation: a -> b -> idle -> idle -> a
"""


def schedule_tasks(tasks, k):
    """
    You are given a list of tasks that need to be run, in any order, on a server.
    Each task will take one CPU interval to execute but once a task has finished, it has a cooling period
    during which it can’t be run again.

    If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that
    the server needs to finish all tasks. If at any time the server can’t execute any task then it must stay idle.

    Example 1:
    Input: [a, a, a, b, c, c], K=2
    Output: 7
    Explanation: a -> c -> b -> a -> c -> idle -> a

    Example 2:
    Input: [a, b, a], K=3
    Output: 5
    Explanation: a -> b -> idle -> idle -> a
    """
    # TODO: Come back to
    interval_count = 0
    return interval_count


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to schedule_tasks
    print(schedule_tasks([]))
