"""
Smallest

"""
def kthSmallest(root: TreeNode, k: int) -> int:
        stk = []
        cntr = 0
        while root or stk:
            while root:
                stk.append(root)
                root = root.left

            root = stk.pop()
            cntr += 1

            if cntr == k:
                return root.val
            else:
                root = root.right


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to kthSmallest
    print(kthSmallest([]))
