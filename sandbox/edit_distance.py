from pprint import pprint
def edit_distance_r(word1, word2):
    def edit_distance_util(str1, str2, m, n):

        if m == 0:
            return n
        if n == 0:
            return m
        if str1[m-1] == str2[n-1]:
            return edit_distance_util(str1, str2, m-1, n-1)
        else:
            return 1 + min(edit_distance_util(str1, str2, m, n-1),
                    edit_distance_util(str1, str2, m-1, n),
                    edit_distance_util(str1, str2, m-1, n-1))

    return edit_distance_util(word1, word2, len(word1), len(word2))

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    if not m: return n
    if not n: return m

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

    pprint (dp)
    return dp[m][n]
                
if __name__ == '__main__':
    str1 = "english"
    str2 = "hebrew"
    print(edit_distance_r(str1, str2))
    print(edit_distance(str1, str2))