def isInterleave(A, B, C):
    m, n = len(A), len(B)
    if len(C) != (m + n):
        return 0

    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    memo[0][0] = 1

    for i in range(1, m + 1):
        memo[i][0] = memo[i - 1][0] and A[i - 1] == C[i - 1]
    for j in range(1, n + 1):
        memo[0][j] = memo[0][j - 1] and B[j - 1] == C[j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if ((memo[i - 1][j] and A[i - 1] == C[i + j - 1]) or (memo[i][j - 1] and B[j - 1] == C[i + j - 1])):
                memo[i][j] = 1
            else:
                memo[i][j] = 0

    return memo[m][n]
if __name__ == '__main__':
    A = "LgR8D8k7t8KIprKDTQ7aoo7ed6mhKQwWlFxXpyjPkh"
    B = "Q7wQk8rqjaH971SqSQJAMgqYyETo4KmlF4ybf"
    C = "Q7wLgR8D8Qkk7t88KIrpqjarHKD971SqSQJTQ7aoAMgoq7eYd6yETmhoK4KmlQwWFlF4xybXfpyjPkh"
    yes = isInterleave(A,B,C)
    print(yes)