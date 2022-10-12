class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.current = homepage
        self.back_history = []
        self.forward_history = []

    def visit(self, url: str) -> None:
        
        self.back_history.append(self.current)
        self.forward_history = []
        self.current = url
        
        
    def back(self, steps: int) -> str:
        possible = min(steps, len(self.back_history)) 
        while possible:  
            self.forward_history.append(self.current)
            self.current = self.back_history.pop() 
            possible -= 1 
        return self.current

    def forward(self, steps: int) -> str:
        possible = min(steps, len(self.forward_history)) 
        while possible: 
            self.back_history.append(self.current)
            self.current = self.forward_history.pop()
            possible -= 1 
        
        return self.current

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