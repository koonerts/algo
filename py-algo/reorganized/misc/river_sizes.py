"""
Sizes

"""


from collections import deque
def riverSizes(matrix):
    results = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == 1:
                q = deque([(i,j)])
                size = 0

                while q:
                    r, c = q.popleft()
                    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == 1:
                        size += 1
                        matrix[r][c] = 0
                        q.append((r,c+1))
                        q.append((r,c-1))
                        q.append((r+1,c))
                        q.append((r-1,c))
                results.append(size)
    return results



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to riverSizes
    print(riverSizes([]))
