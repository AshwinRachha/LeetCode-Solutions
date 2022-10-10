# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        dummy = first = ListNode(-1)
        second_dummy = second = ListNode(-1)
        
        curr = head
        while curr:
            if curr.val < x:
                first.next = ListNode(curr.val)
                first = first.next
            else:
                second.next = ListNode(curr.val)
                second = second.next
            curr = curr.next
        first.next = second_dummy.next
        return dummy.next