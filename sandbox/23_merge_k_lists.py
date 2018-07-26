# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __repr__(self):
        return '{}->'.format(self.val)

from heapq import heappush
from heapq import heappop

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head, curr = None, None
        for i, chain in enumerate(lists):
            if chain:
                heappush(heap, (chain.val, i))
                lists[i] = chain.next
        while heap:
            val, i = heappop(heap)
            if not head:
                head = ListNode(val)
                curr = head
            else:
                node = ListNode(val)
                curr.next = node
                curr = curr.next
            chain = lists[i]
            if chain:
                heappush(heap, (chain.val, i))
                lists[i] = chain.next
        return head

    def print_list(self, head):
        print('List(', end='')
        while head:
            print(head, end='')
            head = head.next
        print('None)', end='')

if __name__ == '__main__':
    result = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 9, 10, 13, 13, 14, 14, None]
    lists = []
    lists.append(ListNode(1, ListNode(4, ListNode(5))))
    lists.append(ListNode(1, ListNode(3, ListNode(4))))
    lists.append(None)
    lists.append(ListNode(2, ListNode(6)))
    lists.append(ListNode(3, ListNode(9, ListNode(10))))
    lists.append(ListNode(7, ListNode(13, ListNode(14))))
    lists.append(ListNode(2, ListNode(13, ListNode(14))))
    s = Solution()
    head = s.mergeKLists(lists)

    i = 0
    while head:
        assert result[i] == head.val
        i += 1
        head = head.next
