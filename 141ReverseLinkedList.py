# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        slow = head
        fast = head.next
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            if fast.next == None:
                return False
            fast = fast.next.next
        return False