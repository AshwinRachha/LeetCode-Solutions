class MyHashMap:

    def __init__(self):
        
        self.arr_len = 1000
        self.dict = [-1 for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        
        hash_value = key % self.arr_len
        if self.dict[hash_value] == -1:
            self.dict[hash_value] = [[key, value]]
            return 
        for i, lst in enumerate(self.dict[hash_value]):
            if lst[0] == key:
                self.dict[hash_value][i][1] = value
                return
        self.dict[hash_value].append([key, value])
        return
        
    def get(self, key: int) -> int:
        
        hash_value = key % self.arr_len
        if self.dict[hash_value] == -1:
            return -1
        for i, lst in enumerate(self.dict[hash_value]):
            if lst[0] == key:
                return lst[1]
        return -1
    def remove(self, key: int) -> None:
        
        ind = key % self.arr_len
        ind_to_remove = -1
        if self.dict[ind] == -1:
            return
        
        for i, kv_pair in enumerate(self.dict[ind]):
            if kv_pair[0] == key:
                ind_to_remove = i
                break
        if ind_to_remove == -1:
            return
        else:
            del self.dict[ind][ind_to_remove]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)