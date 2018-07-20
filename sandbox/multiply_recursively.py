def multiply(a, b):
    def mult(small, big):
        if small == 0:
            return 0
        elif small == 1:
            return big

        s = small >> 1  # dv by 2
        half_prod = mult(s, big)

        if small % 2 == 0:
            return half_prod + half_prod
        else:
            return half_prod + half_prod + big

    smaller = a if a < b else b
    bigger = a if a > b else b
    return mult(smaller, bigger)


if __name__ == '__main__':
    prod = multiply(8, 4)
    assert prod == 32

    prod = multiply(8, 5)
    assert prod == 40

    prod = multiply(5, 5)
    assert prod == 25
