# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        cur = head.next if head else None
        
        while cur:
            while cur and prev.val == cur.val:
                cur = cur.next
            if prev.next == cur:
                prev = cur
                cur = cur.next
            else:
                prev.next = cur

        return head