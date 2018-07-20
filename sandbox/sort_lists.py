import heapq
from collections import deque

class MyHeap:
   def __init__(self, initial=None, key=lambda x:x):
       self.key = key
       if initial:
           self._data = [(key(item), item) for item in initial]
           heapq.heapify(self._data)
       else:
           self._data = []

   def __len__(self):
       return len(self._data)

   def push(self, item):
       heapq.heappush(self._data, (self.key(item), item))

   def pop(self):
       return heapq.heappop(self._data)[1]

def getNextMin(heap_of_queues):
    while heap_of_queues:
        q = heap_of_queues.pop()
        min_value = q.popleft()
        if q:
            heap_of_queues.push(q)
        yield min_value




if __name__ == '__main__':
    heapOfQueues = MyHeap([deque([1,2,3,4,5]),deque([1,4,603,702]),deque([12,34,52])], lambda x : x[0])
    s = getNextMin(heapOfQueues)
    print(list(s))