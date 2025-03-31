"""
Split_primes

"""

from collections import deque


def split_primes(input_str: str) -> int:
    primes = set()
    for a in range(2, 1000):
        if all(a % p != 0 for p in primes):
            primes.add(a)

    dp = deque([1], maxlen=3)
    for i in range(1, len(input_str) + 1):
        lst = []
        for n, count in zip(range(len(dp), 0, -1), dp):
            if input_str[i - n] != "0" and int(input_str[i - n : i]) in primes:
                lst.append(count)
        dp.append(sum(lst))
    return dp[-1]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to split_primes
    print(split_primes([]))
