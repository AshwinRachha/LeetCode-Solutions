class MyStack:

    def __init__(self):
        
        self.deque1 = deque()
        self.deque2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.deque1.append(x)
        for _ in range(len(self.deque1)-1):
            self.deque1.append(self.deque1.popleft())
    def pop(self) -> int:
        return self.deque1.popleft()
    def top(self) -> int:
        return self.deque1[0]
    def empty(self) -> bool:
        return len(self.deque1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()