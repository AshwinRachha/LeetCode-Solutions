class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize = None)
        def calculate(index, s):
            if index == len(nums) and s == target:
                return 1
            if index == len(nums):
                return 0
            return calculate(index + 1, s + nums[index]) + calculate(index + 1, s - nums[index])
            
        
        return calculate(0, 0)
    