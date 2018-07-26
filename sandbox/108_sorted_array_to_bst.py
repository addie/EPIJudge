# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.val)

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def helper(nums, lo, hi):
            if lo > hi:
                return None

            m = (lo + hi) // 2
            n = TreeNode(nums[m])
            n.left = helper(nums, lo, m-1)
            n.right = helper(nums, m+1, hi)
            return n

        return helper(nums, 0, len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    head = s.sortedArrayToBST([-10,-3,0,5,9])
    print(head)
