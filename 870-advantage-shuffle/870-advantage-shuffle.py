class Solution:
    def binarySearch(self , arr , x):
        low = 0 
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] <= x:low = mid + 1
            else: high = mid - 1
        return low
    
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        n = len(nums1)
        ans = []
        for i in nums2:
            idx = self.binarySearch(nums1 , i)
            if idx == n: idx = 0
            ans.append(nums1[idx])
            nums1.pop(idx)
            n-=1
        return ans
        