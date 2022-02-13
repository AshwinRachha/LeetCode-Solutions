intersect = set()
while headB:
intersect.add(headB)
headB = headB.next
while headA:
if headA in intersect:
return headA
headA = headA.next
return None
if not headA or not headB:
return None
first, second = headA, headB
while first!=second and first and second:
first = first.next
second = second.next
if first == second:
return first
if not first:
first = headB
if not second:
second = headA
return first