def print_spiral(matrix):
    res = []
    if len(matrix) == 0: return res
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        for r in range(top + 1, bottom + 1):
            res.append(matrix[r][right])
        if left < right and top < bottom:
            for c in range(right-1, left-1, -1):
                res.append(matrix[bottom][c])
            for r in range(bottom-1, top, -1):
                res.append(matrix[r][left])
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return res

from pprint import pprint
def create_spiral(n):
    if n < 1: return [[]]
    if n == 1: return [[1]]
    spiral = [[0 for _ in range(n)] for _ in range(n)]
    left, right = 0, n-1
    top, bottom = 0, n-1
    val = 1
    while left <= right and top <= bottom:
        for c in range(left, right):
            spiral[top][c] = val
            val += 1
        for r in range(top, bottom):
            spiral[r][right] = val
            val += 1
        for c in range(right, left, -1):
            spiral[bottom][c] = val
            val += 1
        for r in range(bottom, top, -1):
            spiral[r][left] = val
            val += 1
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    if n % 2:
        mid = n//2
        spiral[mid][mid] = n**2
    return spiral

if __name__ == '__main__':
    print(print_spiral([[1,2,3],
                  [4,5,6],
                  [7,8,9]]))
    pprint(create_spiral(7))