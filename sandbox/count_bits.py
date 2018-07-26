def count_bits(num):
    ans = [0 for _ in range(num+1)]
    i, b = 0, 1
    while b <= num:
        while i < b and i + b <= num:
            ans[i+b] = ans[i] + 1
            i += 1
        i = 0
        b <<= 1
    return ans

if __name__ == '__main__':
    print(count_bits(7))

# 0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4

