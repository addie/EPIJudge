# build an LRU "Least Recently Used" cache class,
# cache should have a fixed size of 10 items,
# if cache size ever needs to go above 10 items,
# the "Least Recently Used" item is evicted from the cache

# put -> string itemName, char[] data blob
# get -> returns char[] data blob, or null if item is not in cache

# when you call get(...) then item moves to front of cache, ie it is most recently used
# to do this efficiently you need to use a hashmap, and a doubly linked list
# doubly linked list node should contain prev ptr, next ptr, and the data blob
# hashmap should have key "item name" and value node that contains the data blob in the doubly linked list

class LRU:
    def __init__(self, ):
        pass

    def put(self, ):
        pass

    def get(self):
        pass


if __name__ == '__main__':
