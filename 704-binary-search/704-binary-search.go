func search(nums []int, target int) int {
    
    start := 0
    end := len(nums) - 1
    
    for start <= end {
        mid := (end + start) >> 1
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    
    return -1
    
}