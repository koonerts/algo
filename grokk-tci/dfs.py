class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root: TreeNode, sum: int) -> bool:

    def dfs(node:TreeNode, curr_sum: int):
        if not node: return False
        curr_sum -= node.val

        # is leaf
        if not (node.left and node.right):
            if curr_sum == 0:
                return True
            else:
                return False
        else:
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, sum)


def find_paths(root: TreeNode, sum: int):
    all_paths = []

    def dfs(node:TreeNode, curr_path: [], curr_sum: int):
        if not node: return
        curr_sum -= node.val
        curr_path.append(node.val)

        # is leaf
        if curr_sum == 0 and not (node.left and node.right):
            all_paths.append(list(curr_path))
        else:
            dfs(node.left, curr_path, curr_sum)
            dfs(node.right, curr_path, curr_sum)

        del curr_path[-1]

    dfs(root, [], sum)

    return all_paths


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


def find_path(root: TreeNode, sequence: list[int]):
    """
    Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
    """
    def dfs(node: TreeNode, path) -> bool:
        if not node: return False
        if not node.left and not node.right:
            return path + [node.val] == sequence
        else:
            return dfs(node.left, path + [node.val]) or dfs(node.right, path + [node.val])

    return dfs(root, [])


def count_paths(root: TreeNode, S: int):
    """
    Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
    Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
    """
    def dfs(node: TreeNode, path_count: int) -> int:
        pass
    return dfs(root, 0)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
