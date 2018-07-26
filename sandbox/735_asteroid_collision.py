class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                if stack[-1] < -new:
                    stack.pop()
                    continue
                elif stack[-1] == -new:
                    stack.pop()
                break
            else:
                stack.append(new)
        return stack

if __name__ == '__main__':
    s = Solution()
    asteroids = [5, 10, -5]
    assert [5, 10] == s.asteroidCollision(asteroids)
    asteroids = [8, -8]
    assert [] == s.asteroidCollision(asteroids)
    asteroids = [10, 2, -5]
    assert [10] == s.asteroidCollision(asteroids)
    asteroids = [-2, -1, 1, 2]
    assert [-2, -1, 1, 2] == s.asteroidCollision(asteroids)
    asteroids = [2, 3, -1, -4]
    assert [-4] == s.asteroidCollision(asteroids)