def exp(num, prefix, i, sum_so_far, curr):
    if i == len(num):
        print(prefix + "=" + str(sum_so_far+int(curr)))
    else:
        if prefix and prefix[-1] == '+':
            sum_so_far += int(curr)
            curr = ''

        exp(num, prefix + num[i], i + 1, sum_so_far, curr + num[i])
        if i + 1 < len(num):
            exp(num, prefix + num[i] + '+', i + 1, sum_so_far, curr + num[i])

def expressions(num):
    assert valid(num), "Input string is not numeric."
    exp(num, '', 0, 0, '')

def valid(s):
    if not s:
        return False
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    expressions("1234")