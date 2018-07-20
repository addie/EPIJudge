from random import randint
from collections import Counter
def offline(a, k):
    i = 0
    res = []
    while i < k:
        r = randint(0,len(a)-1)
        res.append(a[r])
        a[i], a[r] = a[r], a[i]
        i += 1

    return res


if __name__ == '__main__':
    hashmap = Counter([3, 7, 2, 4, 5, 8, 9, 1])
    for _ in range(100000):
        arr = offline([3,7,2,4,5,8,9,1], 4)
        for el in arr:
            hashmap[el] += 1
    for i, key in enumerate(hashmap):
        if i == 0:
            c1 = hashmap[key]
            continue
        c2 = hashmap[key]
        print(c1, c2, c1 - c2)
        c1 = c2
    print(hashmap)