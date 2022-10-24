class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        """
        
        2, 3, 1, 2 - 8, 4
        3, 1, 2 - 6
        3, 1, 2, 4 - 10, 4
        1, 2, 4 - 7, 3
        2, 4, 3 - 9, 3
        4, 3
        
        """
        
        start, end, n = 0, 0, len(nums)
        minimum, prefixSum = float('inf'), 0
        while end < n:
            prefixSum += nums[end]
            while prefixSum >= target:
                minimum = min(minimum, end - start + 1)
                prefixSum -= nums[start]
                start += 1
            end += 1
        return minimum if minimum != float('inf') else 0