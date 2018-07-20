def count_inversions(arr):
    def count(arr, left, right):
        inversions = 0
        res = [0] * (right-left)
        if right > left:
            mid = (right + left) // 2
            inversions = count(arr, left, mid) + \
                            count(arr, mid+1, right) + \
                            merge(arr, res, left, mid+1, right)
        return inversions

    def merge(arr, res, left, mid, right):
        i = left
        j = mid
        k = left
        inversions = 0
        while i < mid and j < right:
            if arr[i] <= arr[j]:
                res[k] = arr[i]
                i += 1
            else:
                res[k] = arr[j]
                j += 1
                inversions += mid-i
            k += 1
        while i < mid:
            res[k] = arr[i]
            i += 1
            k += 1
        while j < right:
            res[k] = arr[j]
            j += 1
            k += 1
        return inversions
    return count(arr, 0, len(arr))

if __name__ == '__main__':
    print(count_inversions([1,2,4,6,8]))