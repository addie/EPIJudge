def roman_to_int(roman):
    r2i = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    num = 0
    i = 0
    while i < len(roman):
        if i+1 < len(roman) and r2i[roman[i]] < r2i[roman[i+1]]:
            num += r2i[roman[i+1]] - r2i[roman[i]]
            i += 2
        else:
            num += r2i[roman[i]]
            i += 1

    return num


if __name__ == '__main__':
    print(roman_to_int('MMCCCXLV'))