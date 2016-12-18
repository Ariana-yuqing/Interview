# Leetcode 83 (similar)


from util import LinkedListNode


# Use extra memory, O(n) time, O(n) space
def remove_dups(head):
    if head is None:
        return None
    hs = set()
    hs.add(head.val)
    prev = head
    cur = head.next
    while cur:
        if cur.val not in hs:
            hs.add(cur.val)
            prev.next = cur
            prev = prev.next
        cur = cur.next
    prev.next = None

    return head


# Without extra memory, O(n^2) time, O(1) space
def remove_dups_2(head):
    if head is None:
        return None
    cur = head

    while cur:
        dup = cur
        v = cur.val
        while dup.next:
            if dup.next.val == v:
                dup.next = dup.next.next
            else:
                dup = dup.next
        cur = cur.next
    return head


def main():
    l1 = LinkedListNode.construct_linked_list([1, 2, 3, 4, 2, 1, 3, 3, 1])
    l2 = LinkedListNode.construct_linked_list([1, 2, 2, 4, 2, 1, 1, 6, 1, 7, 8, 7, 6])

    l1.print_linked_list()
    l1_no_dup = remove_dups(l1)
    l1_no_dup.print_linked_list()
    print("----")
    l2.print_linked_list()
    l2_no_dup = remove_dups(l2)
    l2_no_dup.print_linked_list()

    print("_____________ without extra memory")
    l3 = LinkedListNode.construct_linked_list([1, 2, 3, 4, 2, 1, 3, 3, 1])
    l4 = LinkedListNode.construct_linked_list([1, 2, 2, 4, 2, 1, 1, 6, 1, 7, 8, 7, 6])

    l3.print_linked_list()
    l3_no_dup = remove_dups_2(l3)
    l3_no_dup.print_linked_list()
    print("----")
    l4.print_linked_list()
    l4_no_dup = remove_dups(l4)
    l4_no_dup.print_linked_list()

if __name__ == '__main__':
    main()