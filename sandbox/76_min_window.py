import collections
class Solution:
    def minWindow(self, s, t):
        left, right = 0, 0
        counter = collections.defaultdict(int)
        for a in t:
            counter[a] += 1

        minwindow = len(s) + 1
        answer = None

        while right <= len(s):
            # check all chars in T are in the current answer
            if all(map(lambda x: True if x <= 0 else False, counter.values())):
                if minwindow > right - left:
                    minwindow = right - left
                    answer = s[left:right]
                char = s[left]
                if char in counter:
                    counter[char] += 1
                left += 1
            else:
                if right == len(s):
                    break
                char = s[right]
                if char in counter:
                    counter[char] -= 1
                right += 1

        return answer if answer else ''


if __name__ == '__main__':
    a = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    w = a.minWindow(s, t)
    print(w)
