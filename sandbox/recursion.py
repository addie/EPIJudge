from pprint import pprint

def n_queens(n):
    def n_queens_solver(row):
        if n == row:
            result.append(column[n])
            return
        for col in xrange(n):
            for i, c in enumerate(column[:row]):
                if abs(c-col) not in (0, row - i):
                    column[row] = col
                    n_queens_solver(row + 1)

    result, column = [], ([0] * n)
    n_queens_solver(0)
    return result


def generate_permutations(s):
    def permute(i):
        if i == len(s)-1:
            all_permutations.append(''.join(s[:]))
            return

        for j in  xrange(i, len(s)):
            s[i],s[j] = s[j], s[i]
            permute(i + 1)
            s[i], s[j] = s[j], s[i]

    all_permutations = []
    permute(0)
    return all_permutations

def print_subsets(s):
    def subset(set, read, single_subset, write):
        if read == len(set):
            one_subset = []
            for i in xrange(write):
                one_subset.append(single_subset[i])
            subsets.append(one_subset)
            return

        subset(set, read + 1, single_subset, write)
        single_subset[write] = set[read]
        write += 1
        read += 1
        subset(set, read, single_subset, write)

    each_subset = [None] * len(s)
    subsets = []
    subset(s, 0, each_subset, 0)
    return subsets

def best_path(matrix):
    def path(m, i, j):
        if i == 0 and j == 0:
            return m[0][0]
        if i == 0:
            return m[i][j] + path(m, i, j-1)
        if j == 0:
            return m[i][j] + path(m, i-1, j)
        return m[i][j] + max(path(m, i-1, j), path(m, i, j-1))
    return path(matrix, len(matrix)-1, len(matrix[0])-1)


# Diameter = longest path between 2 nodes in a weighted tree
# To get tree diameter we call recursively to each subtree
# Have each subtree return its longest distance to the leaf and its max diameter
# we need both in case the max diameter is in the subtree
class TreeNode:
    def __init__(self, distance=0, children=None):
        self.distanceToParent = distance
        self.children = children

class DiameterAndHeight:
    def __init__(self, diam = -1, height = 0):
        self.diameter = diam
        self.height = height

def diameterX(tree):
    def diameterRecursion(t):
        if not t.children:
            return DiameterAndHeight(0, t.distanceToParent)

        max_diam_and_height = DiameterAndHeight()
        max_height = max_height_2 = 0
        # get the max diameter of all the children and maintain the longest 2 distances
        for child in t.children:
            curr_diam_and_height = diameterRecursion(child)
            max_diam_and_height.diameter = max(max_diam_and_height.diameter, curr_diam_and_height.diameter)
            if curr_diam_and_height.height > max_height:
                max_height_2 = max_height
                max_height = curr_diam_and_height.height
            elif curr_diam_and_height.height > max_height_2:
                max_height_2 = curr_diam_and_height.height

        max_diam_and_height.diameter = max(max_diam_and_height.diameter, max_height + max_height_2)
        max_diam_and_height.longestDistanceToLeaf = max_height + t.distanceToParent
        return max_diam_and_height

    if not tree:
        return -1
    return diameterRecursion(tree).diameter

def diameter(tree):
    def diameter_r(tree):
        if not tree.children:
            ret = DiameterAndHeight()
            ret.diameter = 0
            ret.longestDistanceToLeaf = tree.distanceToParent
            return ret

        ret = DiameterAndHeight()
        longestDist = secondLongestDist = 0
        for child in tree.children:
            curr_diamAndDist = diameter_r(child)







if __name__ == '__main__':
    '''print n_queens(10)
    pprint(generate_permutations(list("1234")))
    matrix =  [[2,8,5,1],
               [3,0,9,3],
               [2,3,1,7],
               [5,5,6,7]]
    pprint (matrix)
    pprint (best_path(matrix))
    print print_subsets([1, 2, 3, 4])'''
    '''
                            x
               [  2                   2  ]
           [ 3       1  ]    [ 1231       9 ]
    
    '''

    n = TreeNode(0,
                 [TreeNode(2,
                           [TreeNode(3), TreeNode(1)]),
                  TreeNode(2,
                           [TreeNode(1231),TreeNode(9)])])
    def dfs(n):
        stack = [n]
        while stack:
            curr = stack.pop()
            print curr.distanceToParent
            if curr.children:
                stack.extend(curr.children)

    dfs(n)
    print diameter(n)

