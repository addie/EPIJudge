class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index = -1
        min_dist = len(words)
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if index != -1 and (word1 == word2 or words[index] != words[i]):
                    min_dist = min(min_dist, i - index)
                index = i
        return min_dist


if __name__ == '__main__':
    s = Solution()
    ans = s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding')
    assert 1 == ans, 'returned {}'.format(ans)