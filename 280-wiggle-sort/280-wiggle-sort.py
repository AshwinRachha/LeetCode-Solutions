class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        first, last = 0, len(temp)-1
        i = 0; switch = False
        while first <= last:
            if not switch:
                nums[i] = temp[first]
                first+=1
            else:
                nums[i] = temp[last]
                last-=1
            i+=1
            switch = not switch
        