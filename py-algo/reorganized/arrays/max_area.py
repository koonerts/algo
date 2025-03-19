"""
Area

"""


def maxArea(heights: list[int]) -> int:
    if not heights or len(heights) <= 1:
        return 0

    def compute_area(x, y):
        if not (0 <= x < len(heights)) or not (0 <= y < len(heights)):
            return 0

        height = min(heights[x], heights[y])
        width = y - x
        return height * width

    left, right, max_area = 0, len(heights) - 1, 0
    while left <= right:
        max_area = max(max_area, compute_area(left, right))
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxArea
    print(maxArea([]))
