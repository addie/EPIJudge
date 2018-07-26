def compare(a, b):
    n, m = len(a), len(b)
    i, j = n-1, m-1
    while i >= 0 and j >= 0:
        if a[i] == '#':
            h = count_hashes(a, i)
            i -= 2*h
        if b[j] == '#':
            h = count_hashes(b, j)
            j -= 2*h
        if i > 0 and j > 0:
            if a[i] != b[j]:
                return False
        i -= 1
        j -= 1

    if i >= 0:
        while a[i] == '#':
            i -= 1
    if j >= 0:
        while b[j] == '#':
            j-= 1

    return True if i < 0 and j < 0 else False

def count_hashes(s, idx):
    count = 0
    while idx >= 0 and s[idx] == '#':
        count += 1
        idx -= 1
    return count

if __name__ == '__main__':
    assert True == compare('abcde##fg', 'abb#cd#fgh#')
    assert False == compare('abcde##f', 'abb#cd#fgh#')
    assert True == compare('####abcde##fg', 'abb#cd#fgh#')
    assert True == compare('abcde##fg', 'abb#cd#fgh#')

