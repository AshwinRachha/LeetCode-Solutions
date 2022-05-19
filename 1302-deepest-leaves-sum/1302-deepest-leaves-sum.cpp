/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    public:    
    int x = 0;
    int depth;
    
    int deepestLeavesSum(TreeNode* root) 
    {
        depth = 1;
        helper(root, 1);
        return x;
    }
    
    void helper(TreeNode* root, int level)
    {
        if(root == NULL)
            return;
        if(level == depth)
            x += root->val;
        else if(level > depth)
        {
            x = root->val;
            depth = level;
        }
        helper(root->left, level + 1);
        helper(root->right, level + 1);
    }
};