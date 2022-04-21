class MyHashSet:
    def __init__(self):
        self.hash_value = 1000
        self.hash_table = [Bucket() for i in range(self.hash_value)]
        
    def add(self, key: int) -> None:
        idx = key % self.hash_value
        self.hash_table[idx].insert(key)
        
    def remove(self, key: int) -> None:
        idx = key % self.hash_value
        self.hash_table[idx].delete(key)
        
    def contains(self, key: int) -> bool:
        idx = key % self.hash_value
        return self.hash_table[idx].exists(key)


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)