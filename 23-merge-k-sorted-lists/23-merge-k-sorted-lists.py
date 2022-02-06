# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        lst = []
        for head in lists:
            while head:
                lst.append(head.val)
                head = head.next
        lst.sort()
        head = dummy = ListNode(None)
        for num in lst:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return head.next
                
        