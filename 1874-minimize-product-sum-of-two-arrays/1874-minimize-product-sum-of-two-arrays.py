import heapq
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1.sort()
        prod = 0
        nums2 = [-x for x in nums2]
        heapq.heapify(nums2)
        for num in nums1:
            prod += heapq.heappop(nums2) * -1 * num
        return prod