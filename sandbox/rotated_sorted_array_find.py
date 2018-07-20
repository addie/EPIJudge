def findMin(a):
    if not a:
        return

    n = len(a)
    lo, hi = 0, n - 1
    while lo <= hi:
        if a[lo] < a[hi]:
            return a[lo]
        m = (hi + lo) // 2
        prev, next = (m - 1) % n, (m + 1) % n
        if a[prev] >= a[m] <= a[next]:
            return a[m]
        if a[m] <= a[hi]:
            hi = m - 1
        elif a[m] >= a[lo]:
            lo = m + 1

if __name__ == '__main__':
    arr = {2,3,5,6,7,8,9,4,3,2,3,7,8,9,6,32,34,23,55,78,9,21,11,11,14,15}
    arr = sorted(list(arr))
    rot = 5
    arr = arr[rot:] + arr[0:rot]
    print(arr)
    mini = findMin(arr)
    print(mini)