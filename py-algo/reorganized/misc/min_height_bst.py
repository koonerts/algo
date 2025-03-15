"""
Height Bst

"""
def minHeightBst(array):
def construct_bst(low, high):
        if low > high:
            return None

        mid = (low+high)//2
        root = BST(array[mid])
        root.left = construct_bst(low, mid-1)
        root.right = construct_bst(mid+1, high)
        return root
    return construct_bst(0, len(array)-1)



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to minHeightBst
    print(minHeightBst([]))
