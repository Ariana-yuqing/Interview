from util import LinkedListNode


def kth_to_last(head, k):
    fast = head
    slow = head

    for i in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


def main():
    l1 = LinkedListNode.construct_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print('1: {}'.format(kth_to_last(l1, 1)))
    print('5: {}'.format(kth_to_last(l1, 5)))
    print('10: {}'.format(kth_to_last(l1, 10)))

    l2 = None
    print('[]: {}'.format(kth_to_last(l2, 2)))


if __name__ == '__main__':
    main()

