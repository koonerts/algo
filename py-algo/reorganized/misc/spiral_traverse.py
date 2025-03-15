"""
Traverse

"""
def spiralTraverse(array):
    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
    direction = RIGHT
    y_left, y_right = 0, len(array[0]) - 1
    x_top, x_bot = 0, len(array) - 1

    result = []
    x, y = 0, 0
    while len(result) < len(array)*len(array[0]):
        if direction == RIGHT:
            y = y_left
            while y_left <= y <= y_right:
                result.append(array[x][y])
                y += 1
            y -= 1
            x_top += 1
        elif direction == DOWN:
            x = x_top
            while x_top <= x <= x_bot:
                result.append(array[x][y])
                x += 1
            x -= 1
            y_right -= 1
        elif direction == LEFT:
            y = y_right
            while y_left <= y <= y_right:
                result.append(array[x][y])
                y -= 1
            y += 1
            x_bot -= 1
        elif direction == UP:
            x = x_bot
            while x_top <= x <= x_bot:
                result.append(array[x][y])
                x -= 1
            x += 1
            y_left += 1
        direction = (direction+1) % 4
    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to spiralTraverse
    print(spiralTraverse([]))
