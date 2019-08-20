# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return None
            
        if not fast:
            return None
        
        while head != slow:
            head = head.next
            slow = slow.next
            
        return slow
        
        