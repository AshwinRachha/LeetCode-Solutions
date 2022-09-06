# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseList(head):
            curr, prev, nxt = head, None, None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        dummy = head = ListNode(-1)
        c = 0
        while l1 or l2:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            c, s = divmod(val1 + val2 + c, 10)
            
            node = ListNode(s)
            head.next = node
            head = node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
         
        if c:
            head.next = ListNode(1)
        return reverseList(dummy.next)
            
        