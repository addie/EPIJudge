def can_jump(nums):
    """
    O(n*k) where k is value in nums
    O(1) space
    :type nums: List[int]
    :rtype: bool
    """
    # [t,f,f,f,f]
    # [t,t,t,t,f]
    # [t,t,t,t,f]
    # DP problem, create dp table can I jump to index i
    can_jump_to = [False for _ in range(len(nums))]
    can_jump_to[0] = True
    # skip last element in top loop, it will be true if set in a prev iteration
    for i in range(len(nums) - 1):
        j = i
        if can_jump_to[i]:
            while j < len(nums) and j - i <= nums[i]:
                can_jump_to[j] = True
                j += 1
    return can_jump_to[len(nums) - 1]

def can_jump_faster(nums):
    """
    O(n)
    O(1) space
    :type nums: List[int]
    :rtype: bool
    """
    last = len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        last = i if i + nums[i] >= last else last
    return last == 0


if __name__ == '__main__':
    a = [3,2,1,0,4]
    print(can_jump_faster(a))
    a = [2,3,1,1,4]
    print(can_jump_faster(a))
    a = [0,1,2]
    print(can_jump_faster(a))
    a = [1,3,5,1,0,1,1,7,1,1,5,4,3,2,1,0,2]
    print(can_jump_faster(a))