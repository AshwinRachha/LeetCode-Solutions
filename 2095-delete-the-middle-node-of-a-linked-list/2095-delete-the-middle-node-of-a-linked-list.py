# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow_val = slow.val if slow else 0
        fast_val = fast.val if fast else 0
        
        slow.next = slow.next.next
        
        return dummy.next
        
        