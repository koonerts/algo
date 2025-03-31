"""
Find_sum_of_path_numbers

"""
def find_sum_of_path_numbers(root: TreeNode):
def dfs(node: TreeNode, curr_sum: int, digit_concat: str):
        if not node: return 0

        digit_concat += str(node.val)
        if not node.left and not node.right:
            curr_sum += int(digit_concat)
            return curr_sum
        else:
            return dfs(node.left, curr_sum, digit_concat) + dfs(node.right, curr_sum, digit_concat)

    curr_sum = 0
    curr_sum = dfs(root, curr_sum, "")
    return curr_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_sum_of_path_numbers
    print(find_sum_of_path_numbers([]))
