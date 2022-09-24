/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) [][]int {
    result:=make([][]int,0)
    tempArr := make([]int,0)
    dfs(root,targetSum,&result,tempArr)
    return result
}

func dfs(root *TreeNode, sum int, result *[][]int, tempArr []int){
    if root == nil{
        return
    }
    if root.Left == nil && root.Right == nil && root.Val == sum{
        tempArr = append(tempArr, root.Val)
        *result = append(*result, append([]int(nil),tempArr...))
    }
    dfs(root.Left, sum -root.Val, result, append(tempArr, root.Val))
    dfs(root.Right, sum -root.Val, result, append(tempArr, root.Val))
}