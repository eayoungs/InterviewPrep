def count_islands(arr):
    islands = 0
    i = 1
    j = 1
    n = len(arr)
    visited = [[0 for item in range(n)] for item in range(n)]

    end = n - 1
    for i in range(end):
        for j in range(end):
            if arr[i][j] == 0:
                islands += is_island(i, j, visited)


def is_island(i, j, visited):
    map_size = len(visited)
    nebas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for neba in nebas:
        if visited[neba[0]][neba[1]] == 0:
            visited[neba[0]][neba[1]] = 1
            idx = (i + neba[0], j + neba[1])
            if idx[0] == 0 or idx[1] == 0 or \
               idx[0] == map_size or idx[1] == map_size:
                return 0
            else:
                return is_island(neba[0], neba[1], visited)
        else:
            return 1
