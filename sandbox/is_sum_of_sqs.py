def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    a, b = 0, c
    done = False
    while not done:
        if a == b:
            done = True

        sum_of_sqs = (a ** 2 + b ** 2)
        if sum_of_sqs == c:
            return True
        elif sum_of_sqs > c:
            b -= 1
        elif sum_of_sqs < c:
            a += 1

        if done:
            break

    return False

import math
def judgeSquareSumFaster(c):
    """
    :type c: int
    :rtype: bool
    """
    a = b = math.floor(math.sqrt(c))
    sum_of_sqs = (a ** 2 + b ** 2)
    while ...
        if c == sum_of_sqs
            return True



    return False


if __name__ == '__main__':
    print(judgeSquareSumFaster(10000000))