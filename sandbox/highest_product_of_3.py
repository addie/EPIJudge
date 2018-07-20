def highest_product_of_3(arr):
    if len(arr) < 3:
        return None

    # keep track of hightest products to account for negatives
    max_number = max(arr[0],arr[1])
    min_number = min(arr[0],arr[1])
    max_prod_of_2 = arr[0]*arr[1]
    min_prod_of_2 = arr[0]*arr[1]
    max_prod_of_3 = arr[0]*arr[1]*arr[2]
    for i, num in enumerate(arr):
        if i < 2:
            continue
        max_prod_of_3 = max(max_prod_of_3, num * min_prod_of_2, num * max_prod_of_2)
        max_prod_of_2 = max(max_prod_of_2, max_number*num, min_number*num)
        min_prod_of_2 = min(min_prod_of_2, max_number*num, min_number*num)
        max_number = max(max_number, num)
        min_number = min(min_number, num)

    return max_prod_of_3


if __name__ == '__main__':
    max_prod = highest_product_of_3([-4,36,2,6,-7,3,-1,-35,5,-6,-7,3,1,-23,3,45,6])
    print(max_prod)