"""
Squares

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
"""
def sortedSquares(a: list[int]) -> list[int]:
        """
        Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        """

        ret = []
        l, r = 0, 0
        while r < len(a) and a[r] < 0:
            r += 1
        l = r - 1

        while len(ret) != len(a):
            if l < 0 or l >= len(a):
                ret.append(a[r] ** 2)
                r += 1
            elif r < 0 or r >= len(a):
                ret.append(a[l] ** 2)
                l -= 1
            else:
                if abs(a[l]) <= abs(a[r]):
                    ret.append(a[l] ** 2)
                    l -= 1
                else:
                    ret.append(a[r] ** 2)
                    r += 1

        return ret


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to sortedSquares
    print(sortedSquares([]))
