class Trie:
    class TrieNode:
        def __init__(self, label=None, data=None):
            self.label = label
            self.data = data
            self.children = []

        def __getitem__(self, key):
            return self.children[key]

        def add_child(self, key, data):
            if self.children:
                self.children.append()

    def __init__(self):
        pass

    def insert(self, word):
        pass

    def search(self, word):
        pass