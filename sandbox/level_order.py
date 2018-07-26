from collections import deque
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
    def __str__(self):
        return 'Node({})'.format(self.val)

def level_order(root):
    if not root:
        return None
    q = deque()
    start = root
    q.append((start, 0))
    res = []
    while q:
        n_tup = q.popleft()
        node = n_tup[0]
        level = n_tup[1]
        if len(res) == level:
            res.append([n_tup[0].val])
        else:
            res[level].append(n_tup[0].val)
        for child in node.children:
            q.append((child, level + 1))

    return res

if __name__ == '__main__':
    # [[1], [3, 2, 4], [5, 6]]
    n5, n6 = Node(5,[]), Node(6,[])
    n3 = Node(3, [n5, n6])
    n = Node(1, [n3,Node(2,[]),Node(4,[])])
    print(level_order(n))