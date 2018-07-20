from pprint import pprint
def minimumDeleteSum(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: int
    """
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] + ord(s1[i])

    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] + ord(s2[j])

    pprint(dp)
    for x in range(len(s1) + 1):
        for y in range(len(s2) + 1):
            pass

if __name__ == '__main__':
    assert 231 == minimumDeleteSum("sea", "eat")
    assert 403 == minimumDeleteSum("delete", "leet")

    [[0, 0, 0, 313],
     [0, 0, 0, 198],
     [0, 0, 0, 97],
     [314, 213, 116, 0]]
