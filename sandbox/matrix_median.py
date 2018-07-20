from bisect import bisect_right

class Solution:
    # @param A : list of list of integers
    # @return an integer
    @staticmethod
    def findMedian(matrix):
        def calc_bounds(m):
            mi = m[0][0]
            mx = m[0][-1]
            for r in range(1, len(matrix)):
                mi = min(mi, matrix[r][0])
                mx = max(mx, matrix[r][-1])
            return mi, mx

        r, c = len(matrix), len(matrix[0])
        mi, mx = calc_bounds(matrix)
        desired = (r * c + 1) // 2
        while mi < mx:
            mid = mi + (mx - mi) // 2
            num_smaller_mid = 0

            # Find count of elements smaller than mid
            for i in range(r):
                j = bisect_right(matrix[i], mid)
                num_smaller_mid = num_smaller_mid + j
            if num_smaller_mid < desired:
                mi = mid + 1
            else:
                mx = mid

        return mi

if __name__ == '__main__':
    m = [[1, 3, 5],
         [2, 6, 9],
         [3, 6, 9]]

    print(Solution.findMedian(m))
