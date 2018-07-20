class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)

        if n == 0:
            return []

        A.reverse()
        carry = self.addOne(A, 0)
        i = 1
        while i < n and carry:
            carry = self.addOne(A, i)
            i += 1

        if carry:
            A.append(1)

        A.reverse()

        i = 0
        while A[i] == 0:
            i += 1
        return A[i:]

    def addOne(self, A, i):
        carry = False
        curr = A[i]
        if curr == 9:
            carry = True
            curr = 0
        else:
            curr += 1
        A[i] = curr
        return carry


if __name__ == '__main__':
    s = Solution()
    A = [ 1, 9, 9, 9, 9, 9, 9 ]
    print(s.plusOne(A))