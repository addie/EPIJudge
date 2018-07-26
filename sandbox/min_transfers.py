# A group of friends went on holiday and sometimes lent each other money.
# For example, Alice paid for Bill's lunch for $10. Then later Chris gave
# Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z)
# which means person x gave person y $z. Assuming Alice, Bill, and Chris
# are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID),
# the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

# Given a list of transactions between a group of people, return the minimum
# number of transactions required to settle the debt.

# Note:

# A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or
# we could also have the persons 0, 2, 6.
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

# Output:
# 1

# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.

# Therefore, person #1 only need to give person #0 $4, and all debt is settled.

def min_transfers(transactions):
    counter = collections.Counter()
    for f, t, m in transactions:
        counter[f] -= m
        counter[t] += m
    balances = list(counter.values())

    def dfs(b):
        if not b:
            return 0
        if not b[0]:
            return dfs(b[1:])
        for i in range(1, len(b)):
            if b[i] == -b[0]:
                return 1 + dfs(b[1:i] + [0] + b[i + 1:])
        ret = []
        for i in range(1, len(b)):
            if b[i] * b[0] < 0:
                ret.append(dfs(b[1:i] + [b[i] + b[0]] + b[i + 1:]))
        return 1 + min(ret)

    return dfs(balances)

if __name__ == '__main__':
