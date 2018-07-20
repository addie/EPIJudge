from pprint import pprint


def permutations(nums):
    def perm(nums, i):
        if i == len(nums) - 1:
            print(nums)
        else:
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perm(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]  # swap back, for the next

    perm(nums, 0)


def permute_unique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in range(len(l) + 1):
                new_ans.append(l[:i] + [n] + l[i:])
                if i < len(l) and l[i] == n:
                    break  # handles duplication
        ans = new_ans
    return ans


123
456
789
if __name__ == '__main__':
    permutations(list("aaab"))
    print()
    p = permute_unique(list("aaab"))
    for el in p:
        pprint(el)
