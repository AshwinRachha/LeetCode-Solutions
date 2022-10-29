class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        """
        Brute Force
        longest_sequence = 0
        for left in range(len(nums)):
            num_zeros = 0
            for right in range(left, len(nums)):
                if num_zeros == 2:
                    break
                if nums[right] == 0:
                    num_zeros += 1
                if num_zeros <= 1:
                    longest_sequence = max(longest_sequence, right - left + 1)
        return longest_sequence
        """
        
        maximum = 0
        left, right = 0, 0
        k = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                k += 1
                while k == 2:
                    if nums[left] == 0:
                        k -= 1
                    left += 1
            
            maximum = max(maximum, right - left + 1)
        return maximum
        