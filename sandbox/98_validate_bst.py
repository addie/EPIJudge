# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.val)

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(root, min_val, max_val):
            if not root:
                return True

            # left MUST be less than root, right MUST be greater than root
            if root.val >= max_val or root.val <= min_val:
                return False

            return isValid(root.left, min_val, root.val) and isValid(root.right, root.val, max_val)

        return isValid(root, float('-inf'), float('inf'))

    def create_tree(self, root):
        """
        :type root: List[int]
        :rtype: TreeNode
        """
        if not root:
            return None

        def helper(nums, lo, hi):
            if lo > hi:
                return None

            m = (lo + hi) // 2
            n = TreeNode(nums[m])
            n.left = helper(nums, lo, m - 1)
            n.right = helper(nums, m + 1, hi)
            return n

        return helper(root, 0, len(root) - 1)


if __name__ == '__main__':
    s = Solution()
    root = s.create_tree([1,2,3])
    assert True == s.isValidBST(root)