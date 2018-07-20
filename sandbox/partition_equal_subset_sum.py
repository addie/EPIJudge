def can_partition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    """
    example
    [1, 5, 11, 5]
    [1,5,5] [11]
    dp and choose or not choose element
    dp[i][j] stores whether the specific sum j can be gotten from the first i numbers. 
    If we can pick such a series of numbers from 0 to i whose sum is j, dp[i][j] is true, otherwise it is false.
    """
    n = len(nums)
    s = sum(nums)
    if not s % 2 == 0 or not n > 1:
        return False
    s //= 2
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(s + 1):
        dp[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][s]

if __name__ == '__main__':
    print(can_partition([1, 5, 11, 5]))
    print(can_partition([1, 2, 3, 5]))