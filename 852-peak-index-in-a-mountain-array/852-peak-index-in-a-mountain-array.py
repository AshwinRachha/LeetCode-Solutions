class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr)
        while left <= right:
            mid = (left + right) // 2
            if mid == left and arr[mid] < arr[mid+1]:
                return mid + 1
            if mid == right and arr[mid] > arr[mid - 1]:
                return mid
            if arr[mid-1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid-1] > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        