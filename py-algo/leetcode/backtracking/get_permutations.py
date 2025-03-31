"""
Permutations

"""

from collections import deque


def getPermutations(array):
    result = []
    if not array:
        return result

    q = deque([[]])
    for num in array:
        for i in range(len(q)):
            p = q.popleft()
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, num)

                if len(p_copy) == len(array):
                    result.append(list(p_copy))
                else:
                    q.append(p_copy)
    return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to getPermutations
    print(getPermutations([]))
