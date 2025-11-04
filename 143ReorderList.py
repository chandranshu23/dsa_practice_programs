# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Base case: 0, 1, or 2 nodes
        if not head or not head.next or not head.next.next:
            return

        # 1. Find the middle of the list
        # 'slow' will end up being the end of the first half
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Split the list and reverse the second half
        second_head = slow.next
        slow.next = None  # Cut the list in two
        
        prev = None
        curr = second_head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 'prev' is now the head of the reversed second list
        
        # 3. Merge the two lists
        first_head = head
        second_head = prev  # The reversed head
        
        # Weave the lists together
        while second_head:
            # Store next pointers
            l1_next = first_head.next
            l2_next = second_head.next
            
            # Link l1 -> l2
            first_head.next = second_head
            
            # Link l2 -> (next of l1)
            second_head.next = l1_next
            
            # Move pointers forward
            first_head = l1_next
            second_head = l2_next1