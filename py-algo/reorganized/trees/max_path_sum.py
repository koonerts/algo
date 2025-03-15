"""
Path Sum

"""
def maxPathSum(root: TreeNode) -> int:
def find_max_sum(node: TreeNode):
            nonlocal max_sum

            if not node:
                return 0
            else:
                left_gain = max(find_max_sum(node.left), 0)
                right_gain = max(find_max_sum(node.right), 0)
                total_gain = left_gain + right_gain + node.val

                max_sum = max(max_sum, total_gain)
                return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        find_max_sum(root)
        return max_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxPathSum
    print(maxPathSum([]))
