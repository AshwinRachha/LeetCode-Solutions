class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        nums1, nums2 = [], []
        for i, n in enumerate(nums):
            if i % 2 == 0:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        nums1.sort()
        nums2.sort(reverse = True)
        left, right = 0, 0
        len1, len2 = len(nums1), len(nums2)
        ans = []
        while left < len1 or right < len2:
            if left < len1:
                ans.append(nums1[left])
                left += 1
            if right < len2:
                ans.append(nums2[right])
                right += 1
        return ans