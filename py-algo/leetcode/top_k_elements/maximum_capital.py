from heapq import heappop, heappush
from typing import List


def maximum_capital(c, k, capitals, profits):
    current_capital = c
    capitals_min_heap = []
    profits_max_heap = []

    for x in range(0, len(capitals)):
        heappush(capitals_min_heap, (capitals[x], x))

    for _ in range(k):

        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
            c, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, (-profits[i]))

        if not profits_max_heap:
            break

        j = -heappop(profits_max_heap)
        current_capital = current_capital + j

    return current_capital


# Example usage (optional, can be removed or placed under if __name__ == "__main__":)
result = maximum_capital(c=0, k=2, capitals=[0, 1, 1], profits=[1, 2, 3])
print(f"Example 1: Max capital = {result}") # Expected: 4

result2 = maximum_capital(c=0, k=3, capitals=[0, 1, 2], profits=[1, 2, 3])
print(f"Example 2: Max capital = {result2}") # Expected: 6
