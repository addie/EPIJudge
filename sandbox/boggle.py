def solve_boggle_trie(board, words):
    class TrieNode:
        def __init__(self, word=None):
            self.word = word
            self.children = [None] * 26

    class Trie:
        def __init__(self, root=None):
            self.root = root

        def insert(self, word):
            node = self.root
            for c in word:
                char_i = ord(c) - ord('a')
                if not node.children[char_i]:
                    node.children[char_i] = TrieNode()
                node = node.children[char_i]
            node.word = word

        def search(self, word):
            node = self.root
            for c in word:
                char_i = ord(c) - ord('a')
                if node.children[char_i]:
                    node = node.children[char_i]
            return node.word == word

        def starts_with(self, prefix):
            node = self.root
            for c in prefix:
                char_i = ord(c) - ord('a')
                if not node.children[char_i]:
                    return False
                node = node.children[char_i]
            return True

    def dfs(board, curr_str, x, y, trie):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == '#':
            return

        saved_char = board[x][y]
        curr_str += saved_char

        if not trie.starts_with(curr_str):
            return

        if trie.search(curr_str):
            res.add(curr_str)

        board[x][y] = '#'
        dfs(board, curr_str, x + 1, y, trie)
        dfs(board, curr_str, x - 1, y, trie)
        dfs(board, curr_str, x, y + 1, trie)
        dfs(board, curr_str, x, y - 1, trie)
        board[x][y] = saved_char

    trie = Trie(TrieNode())
    for word in words:
        trie.insert(word)

    m = len(board)
    n = len(board[0])
    res = set()
    for i in xrange(m):
        for j in xrange(n):
            dfs(board, '', i, j, trie)
    return list(res)

#def solve_boggle_trie_2(board, words):
class TrieNode:
    def __init__(self, val=None):
        self.value = val
        self.children = [False] * 26

class Trie:
    def __init__(self, root=None):
        self.root = root

    def insert(self, word):
        if not self.root:
            self.root = TrieNode()
        current = self.root
        for c in word:
            c_i = ord(c) - ord('a')
            if not current.children[c_i]:
                current.children[c_i] = TrieNode()
            current = current.children[c_i]
        current.value = word

    def search(self, word):
        pass

    def starts_with(self):
        pass


def dfs():
    pass

if __name__ == '__main__':
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    t = Trie()
    t.insert('oath')
    t.insert('pea')

    for child in t.root.children:
        print child.value

    #res = solve_boggle_trie(board, words)
    #print res