class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return "Node ({})".format(self.val)


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        prev = A
        curr = A.next
        while prev and curr:
            while prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
            prev = prev.next
            curr = prev.next

        return head


if __name__ == '__main__':
    s = Solution()
    A = ListNode(1,
                 ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6)))))))))
    B = s.deleteDuplicates(A)
    while B:
        print(B, end=" ")
        B = B.next
