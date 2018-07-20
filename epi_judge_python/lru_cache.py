from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def appendleft(self, value):
        if self.size == self.capacity:
            raise IndexError('Cannot add node. List at capacity.')
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            temp.prev = self.head
        self.size += 1

    def append(self, value):
        if self.size == self.capacity:
            raise IndexError('Cannot add node. List at capacity.')
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail.next = Node(value)
            self.tail = self.tail.next
            self.tail.prev = temp
        self.size += 1

    def remove(self, value):



    def popleft(self):
        if self.size == 0:
            raise IndexError('Cannot pop from an empty list')
        self.size -= 1
        val = self.head.value
        if self.head.next:
            self.head = self.head.next
        self.head.prev = None
        return val

    def pop(self):
        if self.size == 0:
            raise IndexError('Cannot pop from an empty list')
        self.size -= 1
        val = self.tail.value
        if self.tail.prev:
            self.tail = self.tail.prev
        self.tail.next = None
        return val

class LruCache:
    def __init__(self, capacity):
        self.queue = DoublyLinkedList(capacity)
        self.map = {}
        self.size = 0
        self.capacity = capacity

    def lookup(self, isbn):
        return 0

    def insert(self, isbn, price):
        if self.size == capacity:
            if isbn in self.map:


        self.size -= 1

    def erase(self, isbn):
        return True


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv', run_test))
