class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        total = sum(nums)
        n = len(nums)
        maximum = -1
        start, current = 0, 0
        for end in range(n):
            current += nums[end]
            while current > total - x and start <= end:
                current -= nums[start]
                start += 1
            if current == total - x:
                maximum = max(maximum, end - start + 1)
        
        return n - maximum if maximum != -1 else -1
        
        