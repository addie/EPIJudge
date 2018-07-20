class Solution:
    # @param A : integer
    # @return an integer
    # Returns floor of square root of x
    def sqrt(self, x):
        if x == 0 or x == 1:
            return x

        start = 1
        end = x
        while start <= end:
            mid = (start + end) // 2

            # If x is a perfect square
            if mid * mid == x:
                return mid

            # Since we need floor, we update
            # answer when mid*mid is smaller
            # than x, and move closer to sqrt(x)
            if mid * mid < x:
                start = mid + 1
                ans = mid

            else:

                # If mid*mid is greater than x
                end = mid - 1

        return ans

if __name__ == '__main__':
    s = Solution()
    for i in range(11):
        print(s.sqrt(i),end=' ')