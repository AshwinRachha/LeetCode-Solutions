class OrderedStream:
    def __init__(self, n: int):
        self.arr = [None]*(n)
        self.index = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        ans = []
        while self.index < len(self.arr) and self.arr[self.index]:
            ans.append(self.arr[self.index])
            self.index += 1
        return ans
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)