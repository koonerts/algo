"""
Fruits_into_baskets

Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is
    to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

    You can start with any tree, but you can’t skip a tree once you have started.
    You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both the baskets.

    Example 1:
    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

    Example 2:
    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
                 This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


def fruits_into_baskets(fruits: list[str]) -> int:
    """
    Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is
    to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

    You can start with any tree, but you can’t skip a tree once you have started.
    You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both the baskets.

    Example 1:
    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

    Example 2:
    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
                 This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
    """
    fruit_map = {}
    start, max_ = 0, 0

    for i, f in enumerate(fruits):
        if not fruit_map.get(f):
            fruit_map[f] = 1
        else:
            fruit_map[f] += 1

        while len(fruit_map) > 2:
            if fruit_map[fruits[start]] == 1:
                del fruit_map[fruits[start]]
            else:
                fruit_map[fruits[start]] -= 1

            start += 1

        max_ = max(max_, i - start + 1)

    return max_


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to fruits_into_baskets
    print(fruits_into_baskets([]))
