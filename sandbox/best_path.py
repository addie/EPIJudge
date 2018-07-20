def find_path_recursive(grid):
    def get_path(grid, r, c, path):
        if r < 0 or c < 0 or grid[r][c] == -1:
            return False

        if get_path(grid, r-1, c, path) or get_path(grid, r, c-1, path) or (r == 0 and c == 0):
            path.append([r, c])
            return True

        return False

    path = []
    rows = len(grid)-1
    cols = len(grid[0])-1
    get_path(grid, rows, cols, path)
    return path

def find_path(grid):
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def get_path(grid, r, c, path, cache):
        if r < 0 or c < 0 or grid[r][c] == 'X':
            return False

        p = Point(r,c)
        if p in cache:
            return cache[p]

        success = False
        if get_path(grid, r-1, c, path, cache) or get_path(grid, r, c-1, path, cache) or (r == 0 and c == 0):
            path.append([r, c])
            success = True

        cache[p] = success
        return success

    path = []
    cache = {}
    row = len(grid)-1
    col = len(grid[0])-1
    get_path(grid, row, col, path, cache)
    return path


if __name__ == '__main__':
    grid = [
        ['0', '0', 'X', 'X'],
        ['X', '0', 'X', 'X'],
        ['X', '0', 'X', 'X'],
        ['X', '0', 'X', 'X'],
        ['X', '0', '0', 'X'],
        ['X', 'X', '0', '0'],
        ['X', 'X', 'X', '0']
    ]
    print(find_path(grid))