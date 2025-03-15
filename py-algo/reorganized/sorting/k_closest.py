"""
Closest

"""

import math


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    euclidean_dist = lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2)

    min_heap = []
    for point in points:
        if len(min_heap) < k:
            heappush(min_heap, (-euclidean_dist(point), point))
        else:
            curr_euc_dist = euclidean_dist(point)
            if curr_euc_dist < -min_heap[0][0]:
                heappushpop(min_heap, (-curr_euc_dist, point))
    return [tup[1] for tup in min_heap]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to kClosest
    print(kClosest([]))
