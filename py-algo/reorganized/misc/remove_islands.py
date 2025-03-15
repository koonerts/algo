"""
Islands

"""


from collections import deque
def removeIslands(matrix):
    visited = set()
    non_islands = set()
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    for i in [0, len(matrix)-1]:
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                q = deque([(i,j)])
                while q:
                    r, c = q.popleft()
                    visited.add((r,c))
                    non_islands.add((r,c))

                    for d in directions:
                        new_r = r + d[0]
                        new_c = c + d[1]
                        if (new_r, new_c) not in visited and 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] == 1:
                            q.append((new_r, new_c))

    for i in range(len(matrix)):
        for j in [0, len(matrix[0])-1]:
            if (i,j) not in visited and matrix[i][j] == 1:
                q = deque([(i,j)])
                while q:
                    r, c = q.popleft()
                    visited.add((r,c))
                    non_islands.add((r,c))

                    for d in directions:
                        new_r = r + d[0]
                        new_c = c + d[1]
                        if (new_r, new_c) not in visited and 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] == 1:
                            q.append((new_r, new_c))

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if (i,j) not in non_islands and matrix[i][j] == 1:
                matrix[i][j] = 0
    return matrix



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to removeIslands
    print(removeIslands([]))
