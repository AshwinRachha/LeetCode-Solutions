class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n-2):
            k = i + 2
            for j in range(i+1, n-1):
                if nums[i] == 0:
                    continue
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1
        return ans
    
        