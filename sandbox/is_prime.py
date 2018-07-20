import math
def is_prime(n):
    if n in (0, 1):
        return "Not prime"
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return "Not prime"
    return "Prime"

if __name__ == '__main__':
    for i in range(20):
        print(str(i) + " is " + is_prime(i))