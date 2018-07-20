class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, grid):
        def check_duplicates(nine):
            nine_set = set()
            for num in nine:
                if num in nine_set:
                    return False
                nine_set.add(num)

            return True

        def row_valid(grid, row):
            for el in row:


        def col_valid(grid, col):
            for el in col:

        def subgrid_valid(grid, row, col):

            for i in range(9):
                if not row_valid(grid, row):
                    return False

            if not col_valid(grid, col):
                return False

    for i in range(0, 7, 3):  # 0,3,6
        for j in range(0, 7, 3):  # 0,3,6
            if not subgrid_valid(grid, row, col):
                return False

    return True