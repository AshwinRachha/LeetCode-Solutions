func singleNumber(nums []int) int {
    
    ans := 0
    for i := range(nums) {
        ans = ans ^ nums[i]
    }
    return ans
    
}