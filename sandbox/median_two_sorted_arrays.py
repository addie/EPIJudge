
def median(a, b):
    if not a or not b:
        return None

    n, m = len(a), len(b)
    if m < n:
        a, n, b, m = b, m, a, n

    lo, hi = 0, n
    while lo <= hi:
        a_part = (lo + hi) // 2
        b_part = (n + m + 1) // 2 - a_part

        max_left_a = float('-inf') if a_part == 0 else a[a_part-1]
        min_right_a = float('inf') if a_part == n else a[a_part]
        max_left_b = float('-inf') if b_part == 0 else b[b_part-1]
        min_right_b = float('inf') if b_part == m else b[b_part]

        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2
            else:
                return max(max_left_a, max_left_b)
        elif max_left_a > min_right_b:
            hi = a_part - 1
        else:
            lo = a_part + 1

    raise IndexError('Unsorted inputs')

if __name__ == '__main__':
    a = [4, 10, 17, 23]
    b = [2, 6, 9, 41]
    med = median(a, b)
    print(med)

    a = [4, 10, 17, 23]
    b = [2, 6, 9, 41, 56, 100]
    med = median(a, b)
    print(med)

    a = [4, 10, 17, 23]
    b = [2, 6, 9, 41]
    med = median(a, b)
    print(med)

    a = [1,3,4,5]
    b = [6,9,41,56,100]
    med = median(a, b)
    print(med)
