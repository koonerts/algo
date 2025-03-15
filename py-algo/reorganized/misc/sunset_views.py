"""
Views

"""
def sunsetViews(buildings, direction):
    iterator = range(len(buildings)) if direction == 'WEST' else reversed(range(len(buildings)))
    stk = []
    result = []
    for i in iterator:
        if (direction == 'EAST' and i == len(buildings) - 1) or (direction == 'WEST' and i == 0):
            result.append(i)
            stk.append(buildings[i])
        else:
            while stk and stk[-1] < buildings[i]:
                stk.pop()

            if not stk:
                result.append(i)
                stk.append(buildings[i])
    return list(reversed(result)) if direction == 'EAST' else result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to sunsetViews
    print(sunsetViews([]))
