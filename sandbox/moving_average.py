from collections import deque


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.window = deque()
        self.current_sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) < self.size:
            self.current_sum += val
            self.window.append(val)
            return self.current_sum / len(self.window)
        last_val = self.window.popleft()
        self.current_sum += val - last_val
        self.window.append(val)
        return self.current_sum / self.size

    def len(self):
        return len(self.window)

if __name__ == '__main__':
    obj = MovingAverage(3)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))