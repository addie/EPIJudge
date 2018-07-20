class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, xs, lo, hi):
        i = j = 0
        sum = count = 0
        n = len(xs)

        while i < n:
            sum += xs[j]
            if sum >= lo and sum <= hi:
                count += 1
                j += 1
            elif sum < lo:
                j += 1
            elif sum > hi:
                i += 1
                j = i
                sum = 0

            if j == n:
                sum = 0
                i += 1
                j = i

        return count

if __name__ == '__main__':
    A = [80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90]
    B = 99
    C = 269
    s = Solution()
    # print(s.numRange2([1],0,0))
    print(s.numRange2(A,B,C))