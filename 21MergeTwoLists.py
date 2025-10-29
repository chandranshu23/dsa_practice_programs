# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_head = ListNode(-1)
        ptr = dummy_head 
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next  
            else:
                ptr.next = l2
                l2 = l2.next 
            ptr = ptr.next
            
        if l1:
            ptr.next = l1
        elif l2:
            ptr.next = l2
            
        return dummy_head.next