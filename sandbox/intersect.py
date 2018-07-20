class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, a, b):
        a_left = b_left = 0
        a_right, b_right = len(a) - 1, len(b) - 1
        c = []
        while a_left < len(a) and b_left < len(b):
            if a[a_left] < b[b_left]:
                a_left += 1
            elif b[b_left] < a[a_left]:
                b_left += 1
            else:
                c.append(a[a_left])
                a_left += 1
                b_left += 1


        return c

if __name__ == '__main__':
    a  = [1, 3, 8, 10, 13, 13, 16, 16, 16, 18, 21, 23, 24, 31, 31, 31, 33, 35, 35, 37, 37, 38, 40, 41, 43, 47, 47, 48,
        48, 52, 52, 53, 53, 55, 56, 60, 60, 61, 61, 63, 63, 64, 66, 67, 67, 68, 69, 71, 80, 80, 80, 80, 80, 80, 81,
        85, 87, 87, 88, 89, 90, 94, 95, 97, 98, 98, 100, 101]
    b = [5, 7, 14, 14, 25, 28, 28, 34, 35, 38, 38, 39, 46, 53, 65, 67, 69, 70, 78, 82, 94, 94, 98]
    s = Solution()
    print(s.intersect(a, b))