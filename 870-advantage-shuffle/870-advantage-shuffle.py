import bisect
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        n = len(nums1)
        nums1.sort()
        
        for num in nums2:
            
            idx = bisect.bisect_right(nums1, num)
            if idx == n:
                idx = 0
            ans.append(nums1[idx])
            nums1.pop(idx)
            n-=1
        return ans