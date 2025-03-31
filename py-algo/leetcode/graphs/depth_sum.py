"""
Sum

"""
def depthSum(nestedList: list[NestedInteger]) -> int:
def helper(ni_obj, depth):
            if ni_obj.isInteger():
                curr_val = depth * ni_obj.getInteger()
                return curr_val
            else:
                nested_sum = 0
                for nested_ni_obj in ni_obj.getList():
                    nested_sum += helper(nested_ni_obj, depth+1)
                return nested_sum


        depth_sum = 0
        for obj in nestedList:
            depth_sum += helper(obj, 1)
        return depth_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to depthSum
    print(depthSum([]))
