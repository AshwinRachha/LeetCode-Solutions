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
    int ans = 0;
    bool isLeaf(TreeNode* root)
    {
        return root->left == NULL && root->right == NULL;
    }
    void dfs(TreeNode* root, string dir)
    {
        if(root == NULL)
            return;
        if(isLeaf(root) && dir == "left")
            ans += root->val;
        if(root->left != NULL)
            dfs(root->left, "left");
        if(root->right!=NULL)
            dfs(root->right, "right");
    }
    
    int sumOfLeftLeaves(TreeNode* root) 
    {
        dfs(root, "");    
        return ans;
    }
};