class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       self.val = value if value else []

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return type(self.val) == int

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """
       self.val.append(NestedInteger(elem))

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """
       self.val = value

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       return self.val if type(self.val) == int else None

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       return None if type(self.val) == int else self.val

def depthSum(nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """

    def findSum(nestedList, depth):
        ans = 0
        for element in nestedList:
            if element.isInteger():
                ans += element.getInteger() * depth
            else:  # list
                ans += findSum(element.getList(), depth + 1)
        return ans

    return findSum(nestedList, 1)

def depthSumInverse(nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    level = nestedList
    s = []

    while level:
        amt = 0
        next_level = []
        for el in level:
            if type(el) == int:
                amt += el
            else:
                next_level.extend(el)
        level = next_level
        s.append(amt)

    ans = 0
    for i,n in enumerate(s[::-1]):
        ans += (i+1) * n
    return ans

if __name__ == '__main__':
    n = [[1, 1], 2, [1, 1]]
    inv = depthSumInverse(n)
    print(inv)