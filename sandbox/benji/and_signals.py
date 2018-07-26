# Given two lists like
# [t11, t12, t13, t14, ...],
# [t21, t22, t23, t24, ...]

# The values times represent times when
# a digital signal switches from 0 to 1,
# or from 1 to 0, assume both signals
# initially start at 0
#
# output the "and" operation on both
# these signals of the form
# [t1, t2, t3, ...]

# Example
# s1=[  1,  2,  3,  4,  5]
# s2=[0.5,1.0,1.5,2.0,2.5,3.0,3.5]

def and_signals(list1, list2):
    i, j = 0, 0
    m, n = len(list1), len(list2)
    s_i, s_j = 0, 0
    res = []
    signal_set = False
    while i < m and j < n:
        time1, time2 = list1[i], list2[j]
        if time1 < time2:
            s_i = 1 - s_i
            i += 1
        elif time2 < time1:
            s_j = 1 - s_j
            j += 1
        else:
            s_i, s_j = 1 - s_i, 1 - s_j
            i += 1
            j += 1
        if s_i == 1 and s_j == 1 and not signal_set \
           or not (s_i == 1 and s_j == 1) and signal_set:
            signal_set = not signal_set
            res.append(min(time1,time2))
    return res

if __name__ == '__main__':
    a = [1, 2.5, 3, 4, 5]
    b = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4]
    c = and_signals(a, b)
    assert c == [1.5, 2.0, 3.5, 4]

    a = [1,2,3,6,7,8]
    b = [2,5,6,8]
    c = and_signals(a, b)
    assert c == [3,5,7,8]