class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        maximum = 0
        start, end = 0, 0
        dic = defaultdict(int)
        
        for end, fruit in enumerate(fruits):
            dic[fruit] = end
            if len(dic) > 2:
                min_index = min(dic.values())
                start = min_index + 1
                del dic[fruits[min_index]]
            maximum = max(maximum, end - start + 1)
        return maximum
            
        