from collections import defaultdict


def create_trie():
    return defaultdict(create_trie)


class AutocompleteSystem:
    S, T = 0, 1

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = create_trie()
        self.init_add(sentences, times)
        self.prefix = []
        self.output = []

    def init_add(self, sentences, times):
        for sentence, time in zip(sentences, times):
            node = self.trie
            for letter in sentence:
                node = node[letter]
            node[(sentence, time)]

    def add(self, sentence):
        node = self.trie
        for letter in sentence:
            node = node[letter]
        found, times = False, 0
        for key in node:
            if type(key) is tuple and key[0] == sentence:
                found = True
                times = key[1]
        if found:
            del node[(sentence, times)]
            node[(sentence, times + 1)]
        else:
            node[(sentence, 1)]

    def starts_with(self, prefix):
        node = self.trie
        for letter in prefix:
            if letter not in node:
                return []
            node = node[letter]
        return self.find_all(node)

    def find_all(self, root):
        node = root
        for key in node:
            if type(key) is tuple:
                self.output.append(key)
            else:
                self.find_all(node[key])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != '#':
            self.prefix.append(c)
            self.starts_with(self.prefix)
            op = [x[0] for x in sorted(self.output, key=lambda x: (-x[1], x[0]))]
            self.output = []
            return op[:3]
        else:
            self.add(''.join(self.prefix))
            self.prefix = []
            return []

if __name__ == '__main__':

    obj = AutocompleteSystem(["i love you", "island","ironman","i love leetcode","hey"], [5,3,2,2,4])
    print(obj.input('i'))
    print(obj.input(' '))
    print(obj.input('a'))
    print(obj.input('#'))
    print(obj.input('h'))
    print(obj.input('#'))
    print(obj.input('h'))
    print(obj.input('#'))