class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.dummy = self.head = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        
        new_node = ListNode(url)
        self.dummy.next = new_node
        new_node.prev = self.dummy
        self.dummy = new_node

    def back(self, steps: int) -> str:
        
        while steps and self.dummy.prev:
            self.dummy = self.dummy.prev
            steps -= 1
        return self.dummy.val

    def forward(self, steps: int) -> str:
        
        while steps and self.dummy.next:
            self.dummy = self.dummy.next
            steps -= 1
        return self.dummy.val
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

"""

BrowserHistory leetcode - Null
Visit google - Null
Visit facebook - Null
Visit youtube - Null
Back 1 - facebook
Back 1 - google
Forward 1 - facebook
Visit linkedin.com - null
Forward 2 - linkedin
Back 2 - google
Back 7 - leetcode

"""