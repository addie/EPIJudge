import random
from collections import Counter

class RandomPickIndex:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.nums_sorted = sorted(nums)

    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])

    def pickSorted(self, target):
        """
        :type target: int
        :rtype: int
        """
        lo = self.findLo(target)
        hi = self.findHi(target)

        return random.randint(lo, hi)

    def findLo(self, target):
        lo, hi = 0, len(self.nums_sorted) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            if (target == self.nums_sorted[m] and (m - 1 >= 0 and self.nums_sorted[m - 1]) == target) or target < \
                    self.nums_sorted[m]:
                hi = m - 1
            elif target > self.nums_sorted[m]:
                lo = m + 1
            else:
                return m

    def findHi(self, target):
        lo, hi = 0, len(self.nums_sorted) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            if target < self.nums_sorted[m]:
                hi = m - 1
            elif (target == self.nums_sorted[m] and (
                    m + 1 < len(self.nums_sorted) and self.nums_sorted[m + 1]) == target) or target > self.nums[m]:
                lo = m + 1
            else:
                return m

if __name__ == '__main__':
    nums, target = [3,2,1,3,3], 3
    obj = RandomPickIndex(nums)
    mapper = Counter()
    for i in range(100000):
        param_1 = obj.pick(target)
        mapper[param_1] += 1
    print(mapper)