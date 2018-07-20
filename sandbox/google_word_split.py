def word_split(s):
    if not s: return None
    words = []
    memo = {}
    def get_word_prefix(s):
        if not s:
            return True

        if s in memo:
            return memo[s]

        for i in range(1, len(s)+1):
            if is_word(s[:i]):
                memo[s[:i]] = True
                words.append(s[:i])
                if get_word_prefix(s[i:]):
                    return True
                else:
                    words.pop()

        memo[s] = False
        return False

    get_word_prefix(s)
    return words


def is_word(w):
    words = set(['he', 'hell', 'hello', 'how', 'are', 'you', 'oh','war','yo'])
    if w in words:
        return True


if __name__ == '__main__':
    words = word_split('hellohowareyou')
    print(words)