class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    # relative indices
    # [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
    def searchMatrix(self, matrix, k):
        def getMidValue(m, i, rows, cols):
            row = i // cols
            col = i % cols
            return m[row][col]

        if not matrix or not matrix[0]:
            raise ValueError('Need valid matrix as arg')

        r = len(matrix)
        c = len(matrix[0])
        start, end = 0, r * c - 1
        while start <= end:
            mid = (start + end) // 2
            if k == getMidValue(matrix, mid, r, c):
                return 1
            elif k < getMidValue(matrix, mid, r, c):
                end = mid - 1
            elif k > getMidValue(matrix, mid, r, c):
                start = mid + 1

        return 0
