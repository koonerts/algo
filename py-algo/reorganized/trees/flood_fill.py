"""
Fill

"""


def floodFill(
    image: list[list[int]], sr: int, sc: int, new_color: int
) -> list[list[int]]:
    if not image:
        return image

    def fill(x, y, orig_color):
        if (
            x >= len(image)
            or x < 0
            or y >= len(image[x])
            or y < 0
            or image[x][y] != orig_color
            or new_color == orig_color
        ):
            return
        else:
            image[x][y] = new_color
            fill(x, y + 1, orig_color)
            fill(x, y - 1, orig_color)
            fill(x - 1, y, orig_color)
            fill(x + 1, y, orig_color)

    fill(sr, sc, image[sr][sc])
    return image


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to floodFill
    print(floodFill([]))
