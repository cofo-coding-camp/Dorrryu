# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cur_node = head
        dummy_head = ListNode(0)
        dummy_head.next = head

        while cur_node.next:
            comp_node = dummy_head
            while comp_node.next and comp_node.next.val < cur_node.next.val:
                comp_node = comp_node.next
            if cur_node.next != comp_node.next:
                cur_node.next.next, cur_node.next, comp_node.next = comp_node.next, cur_node.next.next, cur_node.next
            else:
                cur_node = cur_node.next
        return dummy_head.next
