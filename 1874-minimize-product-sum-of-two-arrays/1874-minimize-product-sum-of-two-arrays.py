class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1.sort()
        arr = [-num for num in nums2]
        heapq.heapify(arr)
        ans = 0
        
        for i in range(len(nums1)):
            ans += nums1[i] * -1 * heapq.heappop(arr)
        return ans
        