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
    
    int curSum = 0;
    
    void dfs(TreeNode* root)
    {
        if(root == nullptr)
            return;
        dfs(root->right);
        int temp = root->val;
        root->val += curSum;
        curSum += temp;
        dfs(root->left);
    }
    
    TreeNode* convertBST(TreeNode* root) 
    {    
        dfs(root);
        return root;
    }
};