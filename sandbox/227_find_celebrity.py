# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate

def knows(a, b):
    if a in range(0,7) and b == 5:
        return True
    if a == 0 and b == 4 or b == 0 and a == 4:
        return True
    if a == 1 and b == 3 or b == 1 and a == 3:
        return True
    if a == 2 and b == 6 or b == 2 and a == 6:
        return True
    return False

if __name__ == '__main__':
    # knows
    # 0,1,2,3,4,5,6
    #
    s = Solution()
    assert 5 == s.findCelebrity(7), 'function returned {}'.format(s.findCelebrity(7))