class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        while i < len(nums) - 2:
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k-=1
                    while j < k and nums[k] == nums[k + 1]:
                        k-= 1
                elif s < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k-=1
                    while j < k and nums[k] == nums[k + 1]:
                        k-= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
                
        return ans
        