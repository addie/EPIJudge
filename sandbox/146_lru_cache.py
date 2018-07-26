
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'Node({},{})'.format(self.key, self.val)

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def __repr__(self):
        c = self.head
        r = []
        while c:
            r.append(c.val)
            c = c.next
        return '->'.join(r)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            n = self.map[key]
            self.remove(n)
            self.push(n)
            return n.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            n = self.map[key]
            self.remove(n)
            n.val = value
            self.push(n)
            self.map[key] = n
        else:
            n = Node(key, value)
            if len(self.map) >= self.capacity:
                del self.map[self.tail.key]
                self.remove(self.tail)
            self.push(n)
            self.map[key] = n

    def remove(self, n):
        if n.prev:
            n.prev.next = n.next
        else:
            self.head = n.next
        if n.next:
            n.next.prev = n.prev
        else:
            self.tail = n.prev

    def push(self, n):
        n.next = self.head
        n.prev = None
        if self.head:
            self.head.prev = n
        self.head = n
        if not self.tail:
            self.tail = self.head

if __name__ == '__main__':
    a = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    b = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    r = [None,None,1,None,-1,None,-1,3,4]
    obj = LRUCache(2)
    for ins, val, res in zip(a, b, r):
        if ins == 'put':
            obj.put(val[0], val[1])
        elif ins == 'get':
            assert obj.get(val[0]) == res, 'Res is {} but should be {}'.format(obj.get(val[0]), res)
