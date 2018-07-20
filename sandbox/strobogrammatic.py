def find_strobogrammatic_in_range(low, high):
    res, count, l, h = [], 0, int(low), int(high)
    for i in range(len(low), len(high) + 1):
        res += find_strobogrammatic(i)

    for i in range(len(res)):
        if l <= int(res[i]) <= h:
            count += 1

    return count

def find_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # 0: []
    # 1: [1, 8]
    # 2: [11,69,88,96]
    # 3: [111,181,619,689,818,888,916,986]
    # 4: [1111,1691,1881,1961,6119,6699,6889,6969,8118,8698,8888,8968,9116,9696,9886,9966]

    memo = {0: [''], 1: ['0', '1', '8']}
    return helper(n, n, memo)

def helper(m, n, memo):
    if m in memo:
        return memo[m]

    res = []
    nums = helper(m - 2, n, memo)

    for num in nums:
        for pair in ['00', '11', '69', '88', '96']:
            if m == n and pair == '00':
                continue
            res.append(pair[0] + num + pair[1])

    memo[m] = res
    return res

if __name__ == '__main__':
    print(find_strobogrammatic_in_range('1', '100'))