class Solution:
    def generateParenthesis(self, n):
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

if __name__ == '__main__':
    s = Solution()
    p = s.generateParenthesis(3)
    assert ['()()()', '()(())', '(())()', '(()())', '((()))'] == p
    print(p)
