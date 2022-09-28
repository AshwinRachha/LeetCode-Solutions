import "fmt"
func subarraySum(nums []int, k int) int {
    
    dic := make(map[int]int)
    dic[0] = 1
    ans := 0
    prefix := 0
    for i :=  range(nums) {
        prefix += nums[i]
        ans += dic[prefix-k]
        dic[prefix] += 1
    }
    return ans
    
}