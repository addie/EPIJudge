def powerset(myset):
    num = 2 << len(myset)-1
    print(num)


if __name__ == '__main__':
    # {1, 3, 5, 13, 15, 35}
    print(powerset([1,3,5]))