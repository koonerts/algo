"""
Bad Version

:type n: int
        :rtype: int
"""


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1

    mid = (1 + n) // 2
    is_mid_bad = isBadVersion(mid)
    is_prev_good = mid == 1 or not isBadVersion(mid - 1)

    while not (is_mid_bad and is_prev_good):
        if is_mid_bad:
            mid = (1 + (mid - 1)) // 2
        else:
            mid = ((mid + 1) + n) // 2

        is_mid_bad = isBadVersion(mid)
        is_prev_good = mid == 1 or not isBadVersion(mid - 1)

    return mid


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to firstBadVersion
    print(firstBadVersion([]))
