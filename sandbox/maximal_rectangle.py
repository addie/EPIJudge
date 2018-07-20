def maximalRectangle(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0

    cols = len(matrix[0])
    if cols == 0:
        return 0

    max_x = [[0 for _ in range(cols)] for _ in range(rows)]

    area = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if j == 0:
                    max_x[i][j] = 1
                else:
                    max_x[i][j] = max_x[i][j - 1] + 1

                y = 1
                x = cols
                while i - y + 1 >= 0 and matrix[i - y + 1][j] == 1:
                    x = min(x, max_x[i - y + 1][j])
                    area = max(area, x * y)
                    y += 1
    return area

if __name__ == '__main__':
    rect = [[1,1,1],
            [0,1,1],
            [1,0,0]]

    # max = [[1, 2, 3],
    #        [0, 1, 2],
    #        [1, 0, 0]]

    print(maximalRectangle(rect))