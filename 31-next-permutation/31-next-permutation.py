class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        N = len(nums)
        for i in range(N-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return
        swap = N-1
        while nums[pivot-1] >= nums[swap]:
            swap-=1
        nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
        nums[pivot:] = sorted(nums[pivot:])
        return