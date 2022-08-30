/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var ans int
func rangeSumBST(root *TreeNode, low int, high int) int {
    ans = 0
    dfs(root, low, high)
    return ans
}

func dfs(root *TreeNode, low int, high int) {
    if root != nil {
        if root.Val >= low && root.Val <= high {
        ans += root.Val
    }
        if low < root.Val {
            dfs(root.Left, low, high)
        }
        if high > root.Val {
            dfs(root.Right, low, high)
        }
    }
}