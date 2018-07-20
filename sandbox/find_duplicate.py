
def find_duplicate(arr):
    n = len(arr)-1
    sum_inorder = n*(n+1)//2
    return sum(arr) - sum_inorder

def find_first_dup(a):
    for i in range(len(a)):
        val = abs(a[i])
        if a[val-1] < 0:
            return val
        a[val-1] *= -1

    return -1

if __name__ == '__main__':
    # print(find_duplicate([1,3,4,5,6,3,2]))

    print(find_first_dup([2, 3, 3, 1, 5, 2]))
    print(find_first_dup([2, 4, 3, 5, 1]))
    print(find_first_dup([2, 2]))
    print(find_first_dup([2, 3, 3]))
    print(find_first_dup([3, 3, 3]))