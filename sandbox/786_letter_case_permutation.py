class Solution:
    def letterCasePermutation(self, S):
        ans = [[]]
        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)
        return list(map(''.join, ans))

if __name__ == '__main__':
    s = Solution()
    assert ["a1b2", "A1b2", "a1B2", "A1B2"] == s.letterCasePermutation('a1b2')