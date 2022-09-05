class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        if len(nums1) < len(nums2):
            numSet = set(nums1)
            for num in nums2:
                if num in numSet:
                    intersection.add(num)
        else:
            numSet = set(nums2)
            for num in nums1:
                if num in numSet:
                    intersection.add(num)
        
        return list(intersection)
        
        

