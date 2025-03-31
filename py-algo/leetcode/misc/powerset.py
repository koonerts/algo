"""
Powerset

"""


def powerset(array):
    q = [[]]
    for num in array:
        for i in range(len(q)):
            item = q[i].copy()
            item.append(num)
            q.append(item)
    return q


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to powerset
    print(powerset([]))
