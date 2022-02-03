class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        ans = []
        while i < n-3:
            j = i + 1
            while j < n-2:
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1
                    if s > target:
                        right-=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1
                    elif s < target:
                        left+=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                j+=1
                while j < n -2 and nums[j] == nums[j-1]:
                    j+=1
            i+=1
            while i < n - 3 and nums[i] == nums[i-1]:
                i+=1
        return ans

