"""
Kinds Of Node Depths

"""
def allKindsOfNodeDepths(root):
def depths(node, level=0):
        nonlocal total_sum
        if not node:
            return
        else:
            for i in range(1,level+1):
                total_sum += i
            depths(node.left, level+1)
            depths(node.right, level+1)

    total_sum=0
    depths(root)
    return total_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to allKindsOfNodeDepths
    print(allKindsOfNodeDepths([]))
