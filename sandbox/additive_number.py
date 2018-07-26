import itertools
def is_additive(num):
    for i, j in itertools.combinations(range(1, n), 2):
        i1 = int(num[:i])
        i2 = int(num[i:j])
        if i1 + i2