def cut_rod(prices, n):
    def cut(prices, n, cache):
        if n < 1:
            return 0

        max_price = float('-inf')
        for i in range(n):
            current = n-i-1
            if current not in cache:
                cache[current] = cut(prices, current, cache)
            max_price = max(max_price, prices[i] + cache[current])

        return max_price
    return cut(prices, n, {})


def cut_rod_dp(prices, n):
    

if __name__ == '__main__':
    n = 8
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    print(cut_rod(prices, n))

    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    print(cut_rod(prices, n))