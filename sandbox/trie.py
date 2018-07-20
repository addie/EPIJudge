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

from collections import defaultdict

def _trie():
    return defaultdict(_trie)

TERMINAL = None

class WordDictionary(object):
    def __init__(self):
        self.trie = _trie()

    def addWord(self, word):
        trie = self.trie
        for letter in word:
            trie = trie[letter]
        trie[TERMINAL]

    def search(self, word, trie=None):
        if trie is None:
            trie = self.trie
        for i, letter in enumerate(word):
            if letter == '.':
                return any(self.search(word[i+1:], t) for t in trie.itervalues())
            if letter in trie:
                trie = trie[letter]
            else:
                return False
        return TERMINAL in trie

if __name__ == '__main__':
    w = WordDictionary()
    w.addWord('hello')
    w.addWord('hell')
    w.addWord('happy')
    w.addWord('goob')
    w.search('hap')

