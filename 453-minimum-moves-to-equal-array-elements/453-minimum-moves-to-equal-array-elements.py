class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_no = min(nums)
        count = 0
        for num in nums:
            count += num - min_no
        return count