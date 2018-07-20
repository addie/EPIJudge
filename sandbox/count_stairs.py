def count(n):
    if n == 0:
        return 1
    elif n in (1, 2):
        return n

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    return dp[n]


if __name__ == '__main__':
    print(count(15))