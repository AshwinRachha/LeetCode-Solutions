class BrowserHistory:
​
def __init__(self, homepage: str):
self.current = homepage
self.back_history = []
self.forward_history = []
​
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
​
def forward(self, steps: int) -> str:
possible = min(steps, len(self.forward_history))
while possible:
self.back_history.append(self.current)
self.current = self.forward_history.pop()
possible -= 1
return self.current