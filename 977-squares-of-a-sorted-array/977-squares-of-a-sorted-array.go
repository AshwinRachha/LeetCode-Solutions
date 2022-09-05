func sortedSquares(nums []int) []int {
    n := len(nums)
    result := make([]int, n)
    left, right := 0, n-1
    var square int
    for i:= n-1; i >= 0; i-- {
        
        if nums[left] * nums[left] > nums[right] * nums[right] {
            square = nums[left]
            left++
        } else {
            square = nums[right]
            right--
        }
        result[i] = square * square
    }
    return result
}