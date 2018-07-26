class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        pairset = set(map(tuple, pairs))
        # return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset
        #            for w1, w2 in zip(words1, words2))
        for w1, w2 in zip(words1, words2):
            if not (w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset):
                return False


if __name__ == '__main__':
    s = Solution()
    w1 = ['great', 'acting', 'skills']
    w2 = ['fine', 'drama', 'talent']
    pairs =[["great", "fine"], ["acting", "drama"], ["skills", "talent"]]
    s.areSentencesSimilar(w1, w2, pairs)

    w1 = ['great']
    w2 = ['great']
    pairs =[]
    s.areSentencesSimilar(w1, w2, pairs)

    w1 = ["great"]
    w2 = ["doubleplus", "good"]
    pairs = [["great", "doubleplus"]]
    s.areSentencesSimilar(w1, w2, pairs)
