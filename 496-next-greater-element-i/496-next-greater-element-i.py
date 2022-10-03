class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        dic = {}
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                dic[stack[-1]] = num
                stack.pop()
            stack.append(num)
        ans = []
        for num in nums1:
            if num not in dic:
                ans.append(-1)
            else:
                ans.append(dic[num])
        return ans
        