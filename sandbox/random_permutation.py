from random import randint

def random_permutation(arr):
    i, n = 0, len(arr)
    while i < n:
        r = randint(0,n-1)
        arr[i], arr[r] = arr[r], arr[i]
        i += 1
    return arr

def is_perm(a, b):
    return sorted(a) == sorted(b)

if __name__ == '__main__':
    a = [4,5,7,3,2,4,67,65,3,2,13,4,6,7,1]
    perm = random_permutation(a)
    print(is_perm(perm, a), perm)