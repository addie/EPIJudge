# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.

def find_peak(nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        m = (lo + hi) // 2
        if nums[m] > nums[m+1]:
            hi = m
        else:
            lo = m + 1
    return lo


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    assert find_peak(nums) == 2
    nums = [1, 2, 1, 3, 5, 6, 4]
    assert find_peak(nums) == 1 or find_peak(nums) == 5
