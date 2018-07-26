class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            res += 26**i * (ord(s[n-i-1])-ord('A')+1)
        return res

if __name__ == '__main__':
    s = Solution()
    n = s.titleToNumber('BA')
    print(n)