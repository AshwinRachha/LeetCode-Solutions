class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # 1 1 3 4 5
        seen = set()
        start, end = 0, 1
        nums.sort()
        while start < len(nums) and end < len(nums):
            if start!=end and nums[end] - nums[start] == k:
                seen.add((nums[start], nums[end]))
                end+=1
            elif nums[end] - nums[start] < k:
                end+=1
            else:
                start+=1
        return len(seen)
                
                