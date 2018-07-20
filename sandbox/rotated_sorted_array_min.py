class Solution:
    @staticmethod
    def search(a, n):
        def bsearch(a, n, lo, hi):
            while lo <= hi:
                m = (hi + lo) // 2
                if n < a[m]:
                    hi = m - 1
                elif n > a[m]:
                    lo = m + 1
                else:
                    return m

            return -1

        def find_pivot(a):
            n = len(a)
            lo, hi = 0, n - 1
            while lo <= hi:
                if a[lo] < a[hi]:
                    return lo
                m = (hi + lo) // 2
                prev, next = (m - 1) % n, (m + 1) % n
                if a[prev] >= a[m] <= a[next]:
                    return m
                if a[m] <= a[hi]:
                    hi = m - 1
                elif a[m] >= a[lo]:
                    lo = m + 1
        if not a:
            return

        p = find_pivot(a)
        if n == a[p]:
            return p

        if arr[0] < n:
            res = bsearch(a, n, 0, p - 1)
        else:
            res = bsearch(a, n, p + 1, len(a) - 1)

        return res

if __name__ == '__main__':
    # arr = {2,3,5,6,7,8,9,4,3,2,3,7,8,9,6,32,34,23,55,78,9,21,11,11,14,15}
    # arr = sorted(list(arr))
    # rot = 5
    # arr = arr[rot:] + arr[0:rot]
    arr = [7, 8, 9, 11, 14, 15, 21, 23, 32, 34, 55, 78, 2, 3, 4, 5, 6]
    print(arr)
    mini = Solution.search(arr, 21)
    print(mini)