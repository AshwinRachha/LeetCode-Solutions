# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 2 3 4 5
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        count, curr = 0, head
        while curr:
            count += 1
            curr = curr.next
        curr = dummy
        count -= n
        while count > 0:
            count -= 1
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next