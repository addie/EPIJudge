def merge(arr1, arr2):
    i, j, k = 0, 0, 0
    m, n = len(arr1), len(arr2)
    out = []
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1

    while i < m:
        out.append(arr1[i])
        i += 1

    while j < n:
        out.append(arr2[j])
        j += 1

    return out


if __name__ == '__main__':
    a = [1,2,3]
    b = [2,3,4,5,6]
    print (merge(a,b))