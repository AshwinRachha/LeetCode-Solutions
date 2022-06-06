# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        tempA, tempB = headA, headB
        
        while tempA or tempB:
            tempA = headB if tempA == None else tempA
            tempB = headA if tempB == None else tempB
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
        return None
        