"""
Assignment

"""
def taskAssignment(k, tasks):
    idx_map = {}
    for i, v in enumerate(tasks):
        if v not in idx_map:
            idx_map[v] = [i]
        else:
            idx_map[v].append(i)

    tasks.sort()
    lo, hi = 0, len(tasks)-1

    results = []
    while lo < hi:
        v1 = idx_map[tasks[lo]][-1]
        idx_map[tasks[lo]].pop()

        v2 = idx_map[tasks[hi]][-1]
        idx_map[tasks[hi]].pop()

        results.append([v1, v2])

        lo += 1
        hi -= 1
    return results



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to taskAssignment
    print(taskAssignment([]))
