class MyHashSet:

    def __init__(self):
        
        self.dic = defaultdict(bool)
        
    def add(self, key: int) -> None:
        
        self.dic[key] = True

    def remove(self, key: int) -> None:
        
        self.dic[key] = False

    def contains(self, key: int) -> bool:
        
        return self.dic[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)