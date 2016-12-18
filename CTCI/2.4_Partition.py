# Leetcode 86
from util import LinkedListNode


# Use 4 pointers
def partition(head, x):
    cur = head
    lh, lt, rh, rt = None, None, None, None
    while cur:
        if cur.val < x:
            if not lh:
                lh = cur
            else:
                lt.next = cur
            lt = cur
        else:
            if not rh:
                rh = cur
            else:
                rt.next = cur
            rt = cur
        cur = cur.next
    if lt:
        lt.next = rh
    if rt:
        rt.next = None

    return lh if lh else rh


# Use two pointers
def partition2(head, x):
    l = head
    r = head
    while head:
        next = head.next
        if head.val < x:
            head.next = l
            l = head
        else:
            r.next = head
            r = head
        head = next
        r.next = None
    return l

def main():
    print("________Partition 1_______")
    l1 = LinkedListNode.construct_linked_list([3, 5, 8, 5, 10, 2, 1])
    x = 5
    l1_res = partition(l1, x)
    print('Partition at {}: '.format(x), end="")
    l1_res.print_linked_list()
    print("---------")
    l2 = LinkedListNode.construct_linked_list([3, 5, 8, 5, 10, 2, 1])
    x = 0
    l2_res = partition(l2, x)
    print('Partition at {}: '.format(x), end="")
    l2_res.print_linked_list()

    print("________Partition 2_______")
    l1 = LinkedListNode.construct_linked_list([3, 5, 8, 5, 10, 2, 1])
    x = 5
    l1_res = partition2(l1, x)
    print('Partition at {}: '.format(x), end="")
    l1_res.print_linked_list()
    print("---------")
    l2 = LinkedListNode.construct_linked_list([3, 5, 8, 5, 10, 2, 1])
    x = 0
    l2_res = partition2(l2, x)
    print('Partition at {}: '.format(x), end="")
    l2_res.print_linked_list()




if __name__ == '__main__':
    main()