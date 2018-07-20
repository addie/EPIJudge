# def getSubsets(array):
#     def helper(array, subset, i, subsets):
#         if i == len(array):
#             subsets.add(''.join(subset))
#         else:
#             subset[i] = ''
#             helper(array, subset, i+1, subsets)
#             subset[i] = array[i]
#             helper(array, subset, i+1, subsets)
#
#     subsets = set()
#     subset = ['' for _ in range(len(array))]
#     helper(array, subset, 0, subsets)
#     return subsets

def getSubsets(array):
    def helper(array, current, i, subsets):
        if i == len(array):
            subsets.add(''.join(current))
        else:
            current[i] = ''
            helper(array, current, i+1, subsets)
            current[i] = array[i]
            helper(array, current, i+1, subsets)

    subsets = set()
    helper(array, ['']*len(array), 0, subsets)
    return subsets

if __name__ == '__main__':
    print(getSubsets(['a','b','c']))