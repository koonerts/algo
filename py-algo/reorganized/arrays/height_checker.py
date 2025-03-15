"""
Checker

Students are asked to stand in non-decreasing order of heights for an annual photo.
        Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
        Notice that when a group of students is selected they can reorder in any possible way between themselves
        and the non selected students remain on their seats.

        Input: heights = [1,1,4,2,1,3]
        Output: 3

        Input: heights = [5,1,2,3,4]
        Output: 5
"""
def heightChecker(heights: list[int]) -> int:
        """
        Students are asked to stand in non-decreasing order of heights for an annual photo.
        Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
        Notice that when a group of students is selected they can reorder in any possible way between themselves
        and the non selected students remain on their seats.

        Input: heights = [1,1,4,2,1,3]
        Output: 3

        Input: heights = [5,1,2,3,4]
        Output: 5
        """

        heights_sorted = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                cnt += 1
        return cnt


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to heightChecker
    print(heightChecker([]))
