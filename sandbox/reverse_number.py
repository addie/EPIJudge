def reverse(num):
    if -10 < num < 10:
        return num

    if num < 0:
        neg = True
        num = -num

    res = 0
    while num > 0:
        digit = num % 10
        res *= 10
        res += digit
        num //= 10

    return res

if __name__ == '__main__':
    print(reverse(234))