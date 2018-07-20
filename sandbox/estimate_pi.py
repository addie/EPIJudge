#Given that Pi can be estimated using the function
# 4 * (1 – 1/3 + 1/5 – 1/7 + …) with more terms
# giving greater accuracy, write a function that
# calculates Pi to an accuracy of 5 decimal places.
# pi = 3.1415926536

def estimate_pi(n):
    current = 0
    for d in range(1,n,4):
        current += 1/d
        current -= 1/(d+2)
    return 4 * current

if __name__ == '__main__':
    pi = estimate_pi(760000)
    print(pi)