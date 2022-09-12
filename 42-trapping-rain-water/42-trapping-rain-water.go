func trap(height []int) int {
    
    left, right := 0, len(height)-1
    leftMax, rightMax := 0, 0
    res := 0
    
    for left <= right {
        if leftMax < rightMax {
            if leftMax <= height[left] {
                leftMax = height[left]
            } else {
                res += leftMax - height[left]
            }
            left++
        } else {
            if rightMax <= height[right] {
                rightMax = height[right]
            } else {
                res += rightMax - height[right]
            }
            right--
        }
    }
    
    return res
    
}