"""
Two_way_merge

"""
def two_way_merge(arr1, arr2):
        i, j = 0, 0
        result = []
        while i < len(arr1) or j < len(arr2):
            if i >= len(arr1):
                result.append(arr2[j])
                j += 1
            elif j >= len(arr2):
                result.append(arr1[i])
                i += 1
            else:
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
        return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to two_way_merge
    print(two_way_merge([]))
