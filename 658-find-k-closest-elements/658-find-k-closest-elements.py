class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        diff = [(abs(num - x), num) for num in arr]
        heapq.heapify(diff)
        ans = []
        while k:
            ans.append(heapq.heappop(diff)[1])
            k-=1
        return sorted(ans)
        