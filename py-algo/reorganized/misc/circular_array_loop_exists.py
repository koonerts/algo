"""
Circular_array_loop_exists

We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index.
    Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices.
    You should assume that the array is circular which means two things:
        - If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
        - If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

    Write a method to determine if the array has a cycle. The cycle should have more than one element and
    should follow one direction which means the cycle should not contain both forward and backward movements.

    Example 1:

    Input: [1, 2, -1, 2, 2]
    Output: true
    Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

    Example 2:
    Input: [2, 2, -1, 2]
    Output: true
    Explanation: The array has a cycle among indices: 1 -> 3 -> 1

    Example 3:
    Input: [2, 1, -1, -2]
    Output: false
    Explanation: The array does not have any cycle.
"""
def circular_array_loop_exists(arr: list[int]) -> bool:
    """
    We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index.
    Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices.
    You should assume that the array is circular which means two things:
        - If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
        - If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

    Write a method to determine if the array has a cycle. The cycle should have more than one element and
    should follow one direction which means the cycle should not contain both forward and backward movements.

    Example 1:

    Input: [1, 2, -1, 2, 2]
    Output: true
    Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

    Example 2:
    Input: [2, 2, -1, 2]
    Output: true
    Explanation: The array has a cycle among indices: 1 -> 3 -> 1

    Example 3:
    Input: [2, 1, -1, -2]
    Output: false
    Explanation: The array does not have any cycle.
    """
def get_index(curr_index: int, curr_direction: int) -> int:
        new_direction = 1 if arr[curr_index] > 0 else -1
        if new_direction != direction:
            return -1

        new_index = (curr_index + arr[curr_index]) % len(arr)

        if new_index == curr_index:
            return -1
        return new_index

    for i in range(len(arr)):
        slow, fast = i, i
        direction = 1 if arr[i] > 0 else -1

        while True:
            slow = get_index(slow, direction)
            fast = get_index(fast, direction)
            if fast == -1:
                break

            fast = get_index(fast, direction)
            if fast == -1 or slow == -1 or slow == fast:
                break

        if slow == -1 and slow == fast:
            return False
        elif slow == fast:
            return True
    return False



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to circular_array_loop_exists
    print(circular_array_loop_exists([]))
