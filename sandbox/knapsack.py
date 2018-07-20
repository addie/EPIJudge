W = 0
V = 1

def find_optimal_value(weights, values, weight_available):

    # @ k is a map of weight to value
    def find(wts, vals, item, avail):
        if avail == 0 or item == len(wts):
            return 0

        if wts[item] > avail:
            return find(wts, vals, item + 1, avail)

        include_n = vals[item] + find(wts, vals, item + 1, avail - wts[item])
        exclude_n = find(wts, vals, item + 1, avail)

        return max(include_n, exclude_n)

    return find(weights, values, 0, weight_available)

def knapsack(weights, values, weight_avail):
    def ks(weights, values, W, N):
        K = [[0 for _ in range(W+1)] for _ in range(N+1)]
        for n in range(1, N+1):
            for w in range(1, W+1):
                if weights[n-1] > W:
                    K[n][w] = K[n-1][w]
                else:
                    K[n][w] = max(K[n-1][w], values[n-1] + K[n-1][w-weights[n-1]])

        return K[N][W]
    return ks(weights, values, weight_avail, len(values))

if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    weight_available = 50

    optimal = find_optimal_value(weights, values, weight_available)
    print(optimal)

    optimal = knapsack(weights, values, weight_available)
    print(optimal)

