/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, targetSum int) bool {
    ans := depthFirstSearch(root, 0, targetSum)
    return ans
}

func depthFirstSearch(root *TreeNode, currentSum int, targetSum int) bool {
    if root == nil {
        return false
    }
    currentSum += root.Val
    if root.Left == nil && root.Right == nil && currentSum == targetSum {
        return true
    }
    return depthFirstSearch(root.Left, currentSum, targetSum) || depthFirstSearch(root.Right, currentSum, targetSum)
}