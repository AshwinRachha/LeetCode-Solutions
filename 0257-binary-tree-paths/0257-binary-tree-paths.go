func binaryTreePaths(root *TreeNode) []string {
    if root == nil {
        return nil
    }
    result := []string{}
    helper(root, strconv.Itoa(root.Val), &result)
    return result
}

func helper(root *TreeNode, str string, result *[]string) {
    if root.Left == nil && root.Right == nil {
        *result = append(*result, str)
        return
    }
    if root.Left != nil {
        helper(root.Left, str +"->" + strconv.Itoa(root.Left.Val), result)
    }
    if root.Right != nil {
        helper(root.Right, str +"->" + strconv.Itoa(root.Right.Val), result)
    }
}