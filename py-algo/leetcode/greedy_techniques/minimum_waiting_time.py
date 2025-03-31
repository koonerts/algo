"""
Waiting Time

"""


def minimumWaitingTime(queries):
    if not queries:
        return 0

    queries.sort()
    wait_time = queries[0]
    wait_sum = wait_time
    for i in range(1, len(queries) - 1):
        wait_time += queries[i]
        wait_sum += wait_time
    return wait_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to minimumWaitingTime
    print(minimumWaitingTime([]))
