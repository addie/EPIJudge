from collections import defaultdict


def _trie():
    return defaultdict(_trie)


class Trie:
    def __init__(self):
        self.trie = _trie()

    def add(self, word):
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

    def starts_with(self, prefix):
        node = self.trie
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True

    def find_node_ending_with(self, prefix):
        node = self.trie
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return False
        return node

    def count_words_with_prefix(self, node):
        count = 0
        if None in node:
            count += 1
        for k in node:
            count += self.count_words_with_prefix(node[k])
        return count

if __name__ == '__main__':
    t = Trie()
    arr = ["add hack","add hackerrank","find hac","find hak","search hackerrank","starts_with hackerd"]
    for s in arr:
        op, contact = s.split(' ')
        if op == 'add':
            t.add(contact)
        elif op == 'find':
            node = t.find_node_ending_with(contact)
            if node:
                print(t.count_words_with_prefix(node))
            else:
                print(0)
        elif op == 'search':
            print("Found", contact) if t.search(contact) else print(contact, "not found")
        elif op == 'starts_with':
            print("A word starts with",contact) if t.starts_with(contact) else print("no words start with",contact)


