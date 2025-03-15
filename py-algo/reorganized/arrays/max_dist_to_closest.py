"""
Maximum Distance to Closest Person

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the i-th seat, and seats[i] = 0 represents that the i-th seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to the closest person.

Example:
    Input: seats = [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
    If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.
"""


def maxDistToClosest(seats: list[int]) -> int:
    """
    Calculate the maximum possible distance to the closest person in a row of seats.
    
    Args:
        seats (list[int]): A list of 0s and 1s, where 1 represents a person sitting
        
    Returns:
        int: The maximum distance to the closest person
    """
    if not seats:
        return 0
        
    prev = None
    max_dist = 0

    for i in range(len(seats)):
        if seats[i] == 1:
            if prev is None:
                max_dist = i  # Distance from the edge
            else:
                dist = (i - prev) // 2  # Distance between two people
                max_dist = max(max_dist, dist)
            prev = i
    
    # Check the distance from the last person to the end
    if prev is not None and prev < len(seats) - 1:
        max_dist = max(max_dist, len(seats) - 1 - prev)

    return max_dist


# Example usage
if __name__ == "__main__":
    test_cases = [
        [1, 0, 0, 0, 1, 0, 1],  # Expected: 2
        [1, 0, 0, 0],           # Expected: 3
        [0, 1],                 # Expected: 1
        [0, 0, 1]               # Expected: 2
    ]
    
    for seats in test_cases:
        print(f"Seats: {seats}")
        print(f"Max distance to closest person: {maxDistToClosest(seats)}")
        print()