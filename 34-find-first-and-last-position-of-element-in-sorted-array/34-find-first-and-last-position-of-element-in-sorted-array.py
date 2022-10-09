class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(left, right, is_first):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if is_first:
                        if mid == left or nums[mid-1] < target:
                            # This is the first element
                            return mid
                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] > target:
                            return mid
                        left = mid + 1
                        
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return -1
        n = len(nums)
        ans = [binary_search(0,n-1,True), binary_search(0,n-1,False)]
        return ans
        