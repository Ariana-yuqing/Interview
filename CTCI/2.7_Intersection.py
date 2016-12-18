# Leetcode 160
from util import LinkedListNode


def get_tail_and_length(l):
    if not l:
        return 0, None
    length = 1
    cur = l
    while cur.next:
        length += 1
        cur = cur.next
    return length, cur


def intersection(l1, l2):
    n1, last1 = get_tail_and_length(l1)
    n2, last2 = get_tail_and_length(l2)
    if last1.val != last2.val:
        return None

    longer = l1 if n1 > n2 else l2
    shorter = l1 if n1 <= n2 else l2

    k = abs(n1 - n2)

    for i in range(k):
        longer = longer.next

    while longer and shorter:
        if longer.val == shorter.val:
            return longer
        longer = longer.next
        shorter = shorter.next
    return None


def main():
    l1 = LinkedListNode.construct_linked_list([2, 1, 3, 4, 5, 6])
    l2 = LinkedListNode.construct_linked_list([0, 4, 5, 6])
    res = intersection(l1, l2)
    res.print_linked_list()


if __name__ == '__main__':
    main()
