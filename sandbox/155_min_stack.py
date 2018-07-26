# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        if self.m:
            if x < self.m[-1]:
                self.m.append(x)
            else:
                self.m.append(self.m[-1])
        else:
            self.m.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.m.pop()
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m[-1]

# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert -3 == minStack.getMin()
    assert None == minStack.pop()
    assert 0 == minStack.top()
    assert -2 == minStack.getMin()


