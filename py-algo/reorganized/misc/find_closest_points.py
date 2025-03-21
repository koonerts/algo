"""
Find_closest_points

Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

    Example 1:
    Input: points = [[1,2],[1,3]], K = 1
    Output: [[1,2]]
    Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
    The Euclidean distance between (1, 3) and the origin is sqrt(10).
    Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

    Example 2:
    Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
    Output: [[1, 3], [2, -1]]
"""


def find_closest_points(points: list[Point], k: int):
    """
    Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

    Example 1:
    Input: points = [[1,2],[1,3]], K = 1
    Output: [[1,2]]
    Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
    The Euclidean distance between (1, 3) and the origin is sqrt(10).
    Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

    Example 2:
    Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
    Output: [[1, 3], [2, -1]]
    """
    result = []
    for point in points:
        if len(result) < k:
            heappush(result, point)
        elif point.is_closer_to_origin_than(result[0]):
            heappushpop(result, point)

    return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_closest_points
    print(find_closest_points([]))
