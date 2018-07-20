from Trees import *
from collections import namedtuple

def is_balanced(tree):
    HeightBalanced = namedtuple('HeightBalanced', ('balanced','height'))
    def check(tree):
        if not tree:
            return HeightBalanced(True, -1)

        left = check(tree.left)
        if not left.balanced:
            return HeightBalanced(False, 0)

        right = check(tree.right)
        if not right.balanced:
            return HeightBalanced(False, 0)

        is_balanced = abs(left.height - right.height) <= 1
        height = max(left.height, right.height) + 1
        return HeightBalanced(is_balanced, height)

    return check(tree)

if __name__ == '__main__':
    t = deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
    print(is_balanced(t).balanced)