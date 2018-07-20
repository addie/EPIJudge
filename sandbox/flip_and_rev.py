def flip_and_rev(arr):
    def rev(arr):
        i, j = 0, len(arr) - 1
        while i != j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    n = len(arr)
    for i in range(n):
        rev(arr)
        rev(arr[i])

def main():
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    flip_and_rev(arr)
    print(arr)


if __name__ == '__main__':
    main()
