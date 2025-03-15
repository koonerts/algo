"""
Backspace_compare

Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

    Example 1:
    Input: str1="xy#z", str2="xzz#"
    Output: true
    Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

    Example 2:
    Input: str1="xy#z", str2="xyz#"
    Output: false
    Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

    Example 3:
    Input: str1="xp#", str2="xyz##"
    Output: true
    Explanation: After applying backspaces the strings become "x" and "x" respectively.
    In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.

    Example 4:
    Input: str1="xywrrmp", str2="xywrrmu#p"
    Output: true
    Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""
def backspace_compare(str1: str, str2: str) -> bool:
    """
    Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

    Example 1:
    Input: str1="xy#z", str2="xzz#"
    Output: true
    Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

    Example 2:
    Input: str1="xy#z", str2="xyz#"
    Output: false
    Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

    Example 3:
    Input: str1="xp#", str2="xyz##"
    Output: true
    Explanation: After applying backspaces the strings become "x" and "x" respectively.
    In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.

    Example 4:
    Input: str1="xywrrmp", str2="xywrrmu#p"
    Output: true
    Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
    """
    q1, q2 = [], []
def add_or_delete(queue, index, str_):
        if index < len(str_):
            if str_[index] == "#" and queue:
                queue.pop()
            else:
                queue.append(str_[index])

    for i in range(max(len(str1), len(str2))):
        add_or_delete(q1, i, str1)
        add_or_delete(q2, i, str2)

    return q1 == q2



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to backspace_compare
    print(backspace_compare([]))
