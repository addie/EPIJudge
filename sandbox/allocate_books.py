def books(book_list, people):
    def is_possible(arr, readers, curr_min):
        students_required = 1
        curr_sum = 0
        for i in range(len(arr)):
            if arr[i] > curr_min:
                return False
            if curr_sum + arr[i] > curr_min:
                students_required += 1
                curr_sum = arr[i]
                if students_required > readers:
                    return False
            else:
                curr_sum += arr[i]

        return True

    if len(book_list) < people:
        raise ValueError('Num people exceed num books')

    n = sum(book_list)
    lo, hi = 0, n
    res = float('inf')
    while lo <= hi:
        m = (lo + hi) // 2
        if is_possible(book_list, people, m):
            res = min(res, m)
            hi = m - 1  # check smaller
        else:
            lo = m + 1

    return res

if __name__ == '__main__':
    arr = [12, 34, 67, 90]
    m = 2
    print(books(arr, m))