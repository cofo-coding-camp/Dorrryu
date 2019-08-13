# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head
        prev = dummy_head
        cur = head
        
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next == cur:
                prev = prev.next
            else:
                prev.next = cur.next
            cur = cur.next
        return dummy_head.next