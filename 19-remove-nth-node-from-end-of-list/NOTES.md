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