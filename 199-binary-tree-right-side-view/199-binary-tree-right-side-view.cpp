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
    vector<int> rightSideView(TreeNode* root) 
    {
        vector <int> ans;
        if(root == NULL)
            return ans;
        deque <TreeNode*> q;
        q.push_back(root);
        while(!q.empty())
        {
            int size = q.size();
            TreeNode* temp;
            for(int i = 0; i < size; i++)
            {
                temp = q.front(); 
                q.pop_front();
                if(temp->left!=NULL)
                    q.push_back(temp->left);
                if(temp->right!=NULL)
                    q.push_back(temp->right);
            }
            ans.push_back(temp->val);
        }
        return ans;
    }
};