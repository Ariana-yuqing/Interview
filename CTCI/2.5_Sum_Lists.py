# 7->1->6 + 5->9->2 = 617+295 = 912: 2->1->9
from util import LinkedListNode


# Not the best solution, do it in place instead of creating new linked list
def sum_lists(l1, l2):
    res = LinkedListNode(0)
    carry = 0
    p1 = l1
    p2 = l2
    pr = res
    if not p1:
        return p2
    if not p2:
        return p1

    while p1 and p2:
        s = p1.val + p2.val + carry
        # print(p1.val, p2.val, carry, s)
        if s >= 10:
            carry = 1
            s -= 10
        else:
            carry = 0
        # print(p1.val, p2.val, carry, s)
        # print("---")
        pr.next = LinkedListNode(s)
        pr = pr.next
        if p1.next and not p2.next:
            p2.next = LinkedListNode(0)
        elif not p1.next and p2.next:
            p1.next = LinkedListNode(0)
        p1 = p1.next
        p2 = p2.next
    return res.next


def main():
    l1 = LinkedListNode.construct_linked_list([7, 1, 6])
    l2 = LinkedListNode.construct_linked_list([5, 9, 2])
    s = sum_lists(l1, l2)
    print("7->1->6 + 5->9->2 = 617+295 = 912: 2->1->9")
    s.print_linked_list()
    print("---------------")
    l1 = LinkedListNode.construct_linked_list([7, 1, 6, 1, 5, 3])
    l2 = LinkedListNode.construct_linked_list([5, 9, 2])
    s = sum_lists(l1, l2)
    print("7->1->6->1->5->3 + 5->9->2 = 351617+295 = 351912: 2->1->9->1->5->3")
    s.print_linked_list()
    print("---------------")
    l1 = LinkedListNode.construct_linked_list([3])
    l2 = LinkedListNode.construct_linked_list([5, 9, 2])
    s = sum_lists(l1, l2)
    print("3 + 5->9->2 = 3+295 = 298: 8->9->2")
    s.print_linked_list()
    print("---------------")
    l1 = LinkedListNode.construct_linked_list([])
    l2 = LinkedListNode.construct_linked_list([5, 9, 2])
    s = sum_lists(l1, l2)
    print("0 + 5->9->2 = 0+295 = 295: 5->9->2")
    s.print_linked_list()


if __name__ == '__main__':
    main()