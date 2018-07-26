class Solution(object):
    def __init__(self):
        self.map = {
            '1': None,
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res, current_line = [], []
        self.helper(digits, 0, res, current_line)
        return res

    def helper(self, digits, cur, res, line):
        """
        :type digits: str
        :type cur: int
        :type res: List[List[str]]
        :type line: List[str]
        :rtype: None
        """
        if len(line) == len(digits):
            res.append(''.join(line))
            return

        digit = digits[cur]
        for l in self.map[digit]:
            line.append(l)
            self.helper(digits, cur + 1, res, line)
            line.pop()

if __name__ == '__main__':
    s = Solution()
    combos = s.letterCombinations('23')
    assert combos == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    combos = s.letterCombinations('24563')
    assert combos == ['agjmd', 'agjme', 'agjmf', 'agjnd', 'agjne', 'agjnf', 'agjod', 'agjoe', 'agjof', 'agkmd', 'agkme', 'agkmf', 'agknd', 'agkne', 'agknf', 'agkod', 'agkoe', 'agkof', 'aglmd', 'aglme', 'aglmf', 'aglnd', 'aglne', 'aglnf', 'aglod', 'agloe', 'aglof', 'ahjmd', 'ahjme', 'ahjmf', 'ahjnd', 'ahjne', 'ahjnf', 'ahjod', 'ahjoe', 'ahjof', 'ahkmd', 'ahkme', 'ahkmf', 'ahknd', 'ahkne', 'ahknf', 'ahkod', 'ahkoe', 'ahkof', 'ahlmd', 'ahlme', 'ahlmf', 'ahlnd', 'ahlne', 'ahlnf', 'ahlod', 'ahloe', 'ahlof', 'aijmd', 'aijme', 'aijmf', 'aijnd', 'aijne', 'aijnf', 'aijod', 'aijoe', 'aijof', 'aikmd', 'aikme', 'aikmf', 'aiknd', 'aikne', 'aiknf', 'aikod', 'aikoe', 'aikof', 'ailmd', 'ailme', 'ailmf', 'ailnd', 'ailne', 'ailnf', 'ailod', 'ailoe', 'ailof', 'bgjmd', 'bgjme', 'bgjmf', 'bgjnd', 'bgjne', 'bgjnf', 'bgjod', 'bgjoe', 'bgjof', 'bgkmd', 'bgkme', 'bgkmf', 'bgknd', 'bgkne', 'bgknf', 'bgkod', 'bgkoe', 'bgkof', 'bglmd', 'bglme', 'bglmf', 'bglnd', 'bglne', 'bglnf', 'bglod', 'bgloe', 'bglof', 'bhjmd', 'bhjme', 'bhjmf', 'bhjnd', 'bhjne', 'bhjnf', 'bhjod', 'bhjoe', 'bhjof', 'bhkmd', 'bhkme', 'bhkmf', 'bhknd', 'bhkne', 'bhknf', 'bhkod', 'bhkoe', 'bhkof', 'bhlmd', 'bhlme', 'bhlmf', 'bhlnd', 'bhlne', 'bhlnf', 'bhlod', 'bhloe', 'bhlof', 'bijmd', 'bijme', 'bijmf', 'bijnd', 'bijne', 'bijnf', 'bijod', 'bijoe', 'bijof', 'bikmd', 'bikme', 'bikmf', 'biknd', 'bikne', 'biknf', 'bikod', 'bikoe', 'bikof', 'bilmd', 'bilme', 'bilmf', 'bilnd', 'bilne', 'bilnf', 'bilod', 'biloe', 'bilof', 'cgjmd', 'cgjme', 'cgjmf', 'cgjnd', 'cgjne', 'cgjnf', 'cgjod', 'cgjoe', 'cgjof', 'cgkmd', 'cgkme', 'cgkmf', 'cgknd', 'cgkne', 'cgknf', 'cgkod', 'cgkoe', 'cgkof', 'cglmd', 'cglme', 'cglmf', 'cglnd', 'cglne', 'cglnf', 'cglod', 'cgloe', 'cglof', 'chjmd', 'chjme', 'chjmf', 'chjnd', 'chjne', 'chjnf', 'chjod', 'chjoe', 'chjof', 'chkmd', 'chkme', 'chkmf', 'chknd', 'chkne', 'chknf', 'chkod', 'chkoe', 'chkof', 'chlmd', 'chlme', 'chlmf', 'chlnd', 'chlne', 'chlnf', 'chlod', 'chloe', 'chlof', 'cijmd', 'cijme', 'cijmf', 'cijnd', 'cijne', 'cijnf', 'cijod', 'cijoe', 'cijof', 'cikmd', 'cikme', 'cikmf', 'ciknd', 'cikne', 'ciknf', 'cikod', 'cikoe', 'cikof', 'cilmd', 'cilme', 'cilmf', 'cilnd', 'cilne', 'cilnf', 'cilod', 'ciloe', 'cilof']
