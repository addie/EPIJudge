def findContestMatch(n):
    """
    :type n: int
    :rtype: str
    """
    m = list(map(str, range(1, n + 1)))
    while n > 1:
        for i in range(n // 2):
            m[i] = "(" + m[i] + ", " + m[n - 1 - i] + ")"
        n >>= 1
    return m[0]

if __name__ == '__main__':
    assert "(((1, 8), (4, 5)), ((2, 7), (3, 6)))" == findContestMatch(8)