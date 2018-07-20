def parity(x):
    res = 0
    while x:
        res += x & 1
        x >>= 1
    return res % 2

def parity_better(x):
    res = 0
    while x:
        res ^= 1
        x &= x-1
    return res


if __name__ == '__main__':
    for i in range(20):
        print(parity(i), end=' ')
        print(parity_better(i))
