# Leetcode 234


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    if fast and slow:
        slow = slow.next

    while prev:
        if prev.val != slow.val:
            return False
        prev = prev.next
        slow = slow.next
    return True