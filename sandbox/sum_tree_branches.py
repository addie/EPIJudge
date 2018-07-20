# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repl__(self):
        return 'Node({})'.format(self.val)

def sumNumbers(root):
    def sumNums(root, val):
        if not root:
            return 0

        val = val * 10 + root.val  # shift and add

        if not root.left and not root.right:
            return val

        return sumNums(root.left, val) + sumNums(root.right, val)

    return sumNums(root, 0) % 1003

if __name__ == '__main__':
    n1=Node(1)
    n1.left=Node(2)
    n1.left.left=Node(3)
    n1.left.right=Node(4)
    n1.right=Node(3)

    #  12 + 13  =  25
    print(sumNumbers(n1))