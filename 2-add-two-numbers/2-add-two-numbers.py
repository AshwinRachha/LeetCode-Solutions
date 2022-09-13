# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursion(root):
            if not root.next:
                return root.val
            return recursion(root.next) * 10 + root.val
        
        def int_to_linked_list(num: int):
            root = ListNode(num % 10)
            p = root
            num = num // 10
            while num > 0:
                p.next = ListNode(num % 10)
                num = num // 10
                p = p.next
            return root
            
        num1 = recursion(l1)
        num2 = recursion(l2)
        
        return int_to_linked_list(num1 + num2)