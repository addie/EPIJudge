class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return "Node({})".format(self.data)

def merge(A, B):
    node = dh = Node("dummy")
    while A and B:
        if A.data < B.data:
            node.next = A
            node.next.prev = None if node.data == "dummy" else node
            A = A.next
        else:
            node.next = B
            node.next.prev = None if node.data == "dummy" else node
            B = B.next
        node = node.next

    if A:
        A.prev = node
        node.next = A
    else:
        B.prev = node
        node.next = B
    return dh.next


if __name__ == '__main__':
    A = Node(1)
    A.next = a1 = Node(3)
    a1.prev = A
    a1.next = a2 = Node(5)
    a2.prev = a1
    a2.next = a3 = Node(6)
    a3.prev = a2
    a3.next = a4 = Node(7)
    a4.prev = a3

    B = Node(2)
    B.next = b1 = Node(4)
    b1.prev = B

    C = merge(A, B)

    while C:
        print(C)
        t = C
        C = C.next
    while t:
        print(t)
        t = t.prev