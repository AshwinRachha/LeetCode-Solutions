func lengthOfLIS(nums []int) int {
    if len(nums) == 0 { return 0 }

    dp := make([]int, len(nums))

    res := 1
    for i := len(nums)-1; i >= 0; i-- {
        dp[i] = 1
        for j := i + 1; j < len(nums); j++ {
            if nums[j] > nums[i] {
                dp[i] = max(dp[i], 1 + dp[j])
            }
        }
        res = max(res, dp[i])
    }
    return res
}

func max(x, y int) int {
    if x < y { return y }
    return x
}