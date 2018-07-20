def makeMap(s):
    m = {}
    for i, c in enumerate(s):
        if c not in m:
            m[c] = [i]
        else:
            m[c].append(i)
    return m

def check_subsequences(g, s):
    m = makeMap(g)

if __name__ == '__main__':
    s = "bcdefaghabbdadsfk"
