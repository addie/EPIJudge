from heapq import heappush, heappop, heapify

class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n

    def __repr__(self):
        return 'N({})'.format(self.val)

VALUE, INDEX, NODE = 0, 1, 2
def mergeKLists(A):
    if not A:
        return

    head = ListNode(-1, None)  # dummy
    curr = head
    heap = [[A[i].val, i, A[i]] for i in range(len(A))]
    heapify(heap)
    n = len(A)
    while len(heap):
        el = heappop(heap)[NODE]
        curr.next = el
        curr = el
        if el.next:
            heappush(heap, [el.next.val, n, el.next])
            n += 1

    return head.next

def print_list(n):
    while n:
        print('{}->'.format(n.val),end='')
        n = n.next
    print('null')


if __name__ == '__main__':
    # 1 -> 10 -> 20
    # 4 -> 11 -> 13
    # 1 -> 8 -> 9
    l1 = ListNode(1, ListNode(10, ListNode(20, None)))
    l2 = ListNode(4, ListNode(11, ListNode(13, None)))
    l3 = ListNode(1, ListNode(8, ListNode(9, None)))
    n = mergeKLists([l1,l2,l3])
    print_list(n)

