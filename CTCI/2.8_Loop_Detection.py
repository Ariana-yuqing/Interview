# Leetcode 141. Linked List Cycle
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


#  142. Linked List Cycle II
def loop_detection(head):
    """
        :type head: ListNode
        :rtype: ListNode
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow