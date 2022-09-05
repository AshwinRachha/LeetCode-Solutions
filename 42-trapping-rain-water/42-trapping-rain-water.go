func trap(height []int) int {
    
    left, right := 0, len(height) - 1
    leftMax, rightMax := 0, 0
    var res int
    
    for left <= right {
        if leftMax < rightMax {
            if height[left] <= leftMax {
                res += leftMax - height[left]
            } else {
                leftMax = height[left]
            }
            left += 1
        } else {
            if height[right] <= rightMax {
                res += rightMax - height[right]
            } else {
               rightMax = height[right] 
            }
            right -= 1
        }
    }
    
    return res
    
}