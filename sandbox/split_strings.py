def solution(s):
    lis = []
    helper(s, 0, lis)
    return lis


def helper(s, i, lis):
    if i == len(s) - 1:
        lis.append(s[i] + '_')
    elif i >= len(s):
        return
    else:
        lis.append(s[i] + s[i + 1])
    return helper(s, i + 2, lis)

if __name__ == '__main__':
    print(solution('abcdefg'))