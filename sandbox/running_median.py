#!/bin/python3
import sys
import heapq

class MyHeap:
    def __init__(self, key=lambda x:x):
        self.key=key
        self._data=[]

    def push(self, data):
        heapq.heappush(self._data, (self.key(data),data))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def peek(self):
        return self._data[0][1]

    def is_empty(self):
        return False if self._data else True

    def __len__(self):
        return len(self._data)

def add_number(num, lowers, highers):
    if len(lowers) == 0 or num < lowers.peek():
        lowers.push(num)
    else:
        highers.push(num)

def rebalance(lowers, highers):
    while len(lowers) - len(highers) > 1:
        highers.push(lowers.pop())
    while len(highers) - len(lowers) > 1:
        lowers.push(highers.pop())

def get_median(lowers, highers):
    if len(lowers) > len(highers):
        return float(lowers.peek())
    elif len(highers) > len(lowers):
        return float(highers.peek())
    else:
        return (lowers.peek() + highers.peek()) / 2

def get_medians(a):
    lowers = MyHeap(key=lambda x: -x) #maxheap
    highers = MyHeap() #minheap
    medians = [None] * len(a)
    for i, num in enumerate(a):
        add_number(num, lowers, highers)
        rebalance(lowers, highers)
        medians[i] = get_median(lowers, highers)
    return medians

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    m = get_medians(a)
    for num in m:
        print(num)