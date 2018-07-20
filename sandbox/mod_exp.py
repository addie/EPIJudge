def modular_exp(x,n,m):
    def mod(x, n, m, c):
        if n == 0:
            return 1
        if n in c:
            return c[n]
        elif n % 2 == 0:
            cur = int(n/2)
            val = mod(x, cur, m, c)
            c[n] = (val * val) % m
        else:
            cur = int(n-1)
            val = mod(x, cur, m, c)
            c[n] = (x%m * val) % m

        return c[n]
    c = {}
    c[0] = 1
    return mod(x, n, m, c)

if __name__ == '__main__':
    print(modular_exp(71045970,41535484,64735492))