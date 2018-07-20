class Node:
    def __init__(self,x, next):
        self.value = x
        self.next = next

    def __repr__(self):
        return '{}->'.format(self.value)

def merge_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # create dummy node to avoid additional checks in loop
    s = t = Node(None,None)
    while not (head1 is None or head2 is None):
        if head1.value < head2.value:
            # remember current low-node
            c = head1
            # follow ->next
            head1 = head1.next
        else:
            # remember current low-node
            c = head2
            # follow ->next
            head2 = head2.next

        # only mutate the node AFTER we have followed ->next
        t.next = c
        # and make sure we also advance the temp
        t = t.next

    t.next = head1 or head2

    # return tail of dummy node
    return s.next

def print_list(n):
    print('List: ', end=' ')
    while n:
        print(n,end='')
        n = n.next
    print('null')

if __name__ == '__main__':
    l1 = Node(5,Node(8,Node(20,None)))
    l2 = Node(4,Node(11,Node(15,None)))
    n = merge_lists(l1,l2)
    print_list(n)

