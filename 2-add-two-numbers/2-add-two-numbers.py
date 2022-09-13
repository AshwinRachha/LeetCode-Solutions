# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head = ListNode(-1)
        
        c = 0
        
        while l1 or l2:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            c, s = divmod((val1 + val2 + c),10)
            
            node = ListNode(s)
            
            head.next = node
            head = head.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if c:
            node = ListNode(1)
            head.next = node
            
        return dummy.next