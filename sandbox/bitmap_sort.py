import timeit

def bitmap_sort(file):

    lines = 10000000 * [False]
    with open(file) as f:
        for line in f:
            lines[int(line)] = True

    count = 0
    for i, v in enumerate(lines):
        if v:
            count += 1
            print(i)
    print("Count = " + str(count))

if __name__ == '__main__':
    file = 'data/seven_digit_integers'
    bitmap_sort(file)