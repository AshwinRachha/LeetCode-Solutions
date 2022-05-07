class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        elem = float('-inf')
        for num in reversed(nums):
            if num < elem:
                return True
            while stack and stack[-1] < num:
                elem = stack[-1]
                stack.pop()
            stack.append(num)
        return False