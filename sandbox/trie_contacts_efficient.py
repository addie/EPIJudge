class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.size = 0

    def get_index(self, c):
        return ord(c) - ord('a')

    def get_node(self, c):
        return self.children[self.get_index(c)]

    def set_node(self, c, node):
        self.children[self.get_index(c)] = node

    def add(self, s, i=0):
        self.size += 1
        if i == len(s):
            return
        current_letter = s[i]
        child = self.get_node(current_letter)
        if not child:
            child = TrieNode()
            self.set_node(current_letter, child)
        child.add(s, i + 1)

    def find(self, s, i=0):
        if i == len(s):
            return self.size
        current_letter = s[i]
        child = self.get_node(current_letter)
        if not child:
            return 0
        return child.find(s, i + 1)

if __name__ == '__main__':
    t = TrieNode()
    arr = ["add hack","add hackerrank","find hac","find hak"]
    for s in arr:
        op, contact = s.split(' ')
        if op == 'add':
            t.add(contact)
        elif op == 'find':
            print(t.find(contact))
