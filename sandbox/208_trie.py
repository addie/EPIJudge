from collections import defaultdict


def trienode():
    return defaultdict(trienode)


class Trie:

    def __init__(self):
        self.trie = trienode()

    def insert(self, word):
        node = self.trie
        for letter in word:
            node = node[letter]
        node[None]

    def search(self, word):
        node = self.trie
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return None in node

    def startsWith(self, prefix):
        node = self.trie
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert("apple")
    t.search("apple")
    t.search("app")
    t.startsWith("app")
    t.insert("app")
    t.search("app")