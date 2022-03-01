# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []
        for i, l in enumerate(lists):
            if l:
                h.append((l.val, i))        
        heapq.heapify(h)
        head = curr = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
            
        