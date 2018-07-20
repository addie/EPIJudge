def getBiggestRegion(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_count = 0
    for r in range(rows):
        for c in range(cols):
            count = dfs(grid, r, c)
            max_count = max(max_count, count)

    return max_count


def dfs(grid, r, c):
    if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])):
        return 0

    if grid[r][c] == 0:
        return 0

    grid[r][c] = 0

    size = 1
    for x in range(r-1, r+2):
        for y in range(c-1, c+2):
            if x != r or y != c:
                size += dfs(grid, x, y)

    return size

if __name__ == '__main__':
    grid = [[1,1,0,0,0],
            [0,1,1,0,0],
            [0,0,1,0,0],
            [1,0,0,0,0]]
    print(getBiggestRegion(grid))

