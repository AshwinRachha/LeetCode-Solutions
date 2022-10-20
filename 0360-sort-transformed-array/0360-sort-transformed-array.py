class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def apply_quadratic(x):
            return a * x * x + b * x + c
        
        for i in range(len(nums)):
            nums[i] = apply_quadratic(nums[i])
        return sorted(nums)
        