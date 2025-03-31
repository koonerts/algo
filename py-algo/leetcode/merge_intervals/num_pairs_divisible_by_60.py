"""
Num_pairs_divisible_by_60

"""

import collections


def num_pairs_divisible_by_60(times: list[int]) -> int:
    complement = collections.Counter()
    ans = 0
    for t in times:
        if (-t % 60) in complement:
            ans += complement[-t % 60]
        complement[t % 60] += 1
    return ans


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to num_pairs_divisible_by_60
    print(num_pairs_divisible_by_60([]))
