"""
Dist To Closest

"""
def maxDistToClosest(seats: list[int]) -> int:
        prev = None
        max_dist = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                if prev is None:
                    max_dist = i
                else:
                    mid = (prev + i) // 2
                    max_dist = max(max_dist, mid - prev)
                prev = i
            elif i == len(seats) - 1:
                dist = len(seats) - 1 - prev
                max_dist = max(max_dist, dist)

        return max_dist


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxDistToClosest
    print(maxDistToClosest([]))
