def word_break_recursive(word):
    def helper(w, d):
        if w == '':
            return []
        for i in range(1, len(w)+1):
            pre = w[:i]
            if pre in d:
                suf = w[i:]
                remainder = helper(suf, d)
                if remainder is not None:
                    return [pre] + remainder
        return None
    word_dict = {"on", "pi", "pin", "pins", "in", "sand","a", "an", "and", "need", "needle", "needles"}
    return helper(word, word_dict)


def word_break_memo(word):
    def helper(w, d, c):
        # pprint(c)
        if w in c:
            return c[w]
        if w == '':
            return []
        for i in range(1, len(w) + 1):
            pre = w[:i]
            if pre in d:
                suf = w[i:]
                remainder = helper(suf, d, c)
                if remainder is not None:
                    result = [pre] + remainder
                    c[w] = result
                    return result

        c[w] = None
        return None
    word_dict = {"on", "pi", "pin", "pins", "in", "sand", "a", "an", "and", "need", "needle", "needles"}
    cache = {}
    return helper(word, word_dict, cache)

def word_break_dp():
    pass


if __name__ == '__main__':
    print(word_break_recursive('onpinsandneedles'))
    print(word_break_memo('onpinsandneedles'))