# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        if head.next == None:
            return head
        j = head
        k = head.next
        while k.next != None:
            tmp = k.next
            k.next = j
            j = k
            k = tmp
        k.next = j
        head.next = None
        return k

        