# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return 'N({})'.format(self.val)

def detect_cycle(head):
    if not head or not head.next:
        return None
    intersect = get_intersect(head)
    if not intersect:
        return None
    start = head
    while start is not intersect:
        intersect = intersect.next
        start = start.next
    return start

def get_intersect(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return slow
    return None


if __name__ == '__main__':
    a = ListNode('a')
    b = ListNode('b')
    a.next = b
    c = ListNode('c')
    b.next = c
    d = ListNode('d')
    c.next = d
    e = ListNode('e')
    d.next = e
    e.next = c
    assert c is detect_cycle(a)