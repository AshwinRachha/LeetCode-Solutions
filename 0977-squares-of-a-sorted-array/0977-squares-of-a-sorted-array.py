class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n
        left, right = 0, len(nums) - 1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                squared = nums[right]
                right -= 1
            else:
                squared = nums[left]
                left += 1
            res[i] = squared * squared
        return res
        
        
        