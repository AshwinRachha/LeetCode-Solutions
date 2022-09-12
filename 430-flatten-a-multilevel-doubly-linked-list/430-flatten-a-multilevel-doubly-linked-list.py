"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        while current:
            if current.child:
                self.merge(current)
            current = current.next
        return head
    
    def merge(self, current):
        
        child = current.child
        while child.next:
            child = child.next
        
        if current.next:
            child.next = current.next
            current.next.prev = child
        
        current.next = current.child
        current.child.prev = current
        
        current.child = None