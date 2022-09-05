class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        max_area = (right - left) * min(height[left], height[right])
        
        while left < right:
            
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            
        
        return max_area
        