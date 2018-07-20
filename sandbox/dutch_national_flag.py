def dnf(arr, i):
    s, e = 0, len(arr)-1
    m = 0
    pivot = arr[i]
    while m <= e:
        if arr[m] < pivot:
            arr[s], arr[m] = arr[m], arr[s]
            s += 1
            m += 1
        elif arr[m] == pivot:
            m += 1
        else:
            arr[e], arr[m] = arr[m], arr[e]
            e -= 1

    return arr




if __name__ == '__main__':
    #Array in reverse order:
    print(dnf([9, 8, 7, 6, 5, 4, 3, 2, 1], 4))
    #= > [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #Array with only 3 types of elements:
    print(dnf([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2], 4))
    #= > [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]