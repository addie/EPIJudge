def multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise IndexError("Cannot multiply these matrices")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for r in range(rows_a):
        for c in range(cols_b):
            for i in range(cols_a):
                result[r][c] += a[r][i] * b[i][c]
    return result

if __name__ == '__main__':
    a = [[3, -4, 2],[1, 7, -5]]
    b = [[1, 2],[-3, 4],[-5, 6]]

    c = multiply(a, b)
    print(a)
    print(b)
    print(c)
