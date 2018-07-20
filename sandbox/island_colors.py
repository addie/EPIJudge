from collections import deque

NEIGHBORS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def find_max_island(grid):
    if not grid:
        raise IndexError('Not a valid grid')

    visited = set()
    my_stack = deque()
    my_stack.append((0, 0))
    max_count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            current_count = 0
            current_color = grid[r][c]
            while my_stack:
                node = my_stack.pop()
                visited.add(node)
                current_count += 1
                for neighbor in NEIGHBORS:
                    if neighbor not in visited and is_valid(grid, neighbor) and grid[node[0]][node[1]] == current_color:
                        my_stack.append((node[0] + neighbor[0], node[1] + neighbor[1]))
            max_count = max(max_count, current_count)

    return max_count


def is_valid(grid, n):
    return 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0])


def main():
    grid = [
        [1, 1, 2, 3],
        [1, 2, 3, 2],
        [3, 2, 2, 2]
    ]
    print(find_max_island(grid))


if __name__ == 'main':
    main()
