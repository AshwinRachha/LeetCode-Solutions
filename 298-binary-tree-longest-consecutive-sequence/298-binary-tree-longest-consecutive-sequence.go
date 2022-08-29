var ans int

func longestConsecutive(root *TreeNode) int {
    
    ans= 0
    
    if root==nil{
        return 0
    }
    
    helper(root, 1) 
    return ans
    
}

func helper(root *TreeNode, count int) {
    
    ans = max(ans, count)
    
    
    if root.Left!=nil && (root.Left.Val == root.Val + 1) {
        helper(root.Left, count + 1)
    }else{
        if root.Left!=nil{
            helper(root.Left, 1)
        }
    }
    
    if root.Right!=nil && (root.Right.Val== root.Val + 1){
        helper(root.Right, count + 1)
    }else{
        if root.Right!=nil{
            helper(root.Right, 1)
        }
    }
    
}

func max(i, j int) int{
    if i> j{
        return i
    }
    
    return j
}