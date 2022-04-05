class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        ans = 0
        for v in count.values():
            ans += (v * (v-1)) // 2
        return ans