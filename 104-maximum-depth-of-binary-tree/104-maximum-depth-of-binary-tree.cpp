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
    int maxDepth(TreeNode* root) 
    {
        stack <pair<int, TreeNode*>> st;
        int depth = 0;
        if(root!=NULL)
            st.push(pair<int, TreeNode*>(1, root));
        while(!st.empty())
        {
            pair<int, TreeNode*> temp;
            temp = st.top(); st.pop();
            //cout<<temp.first<<endl<<temp.second;
            if(temp.second!=NULL)
            {
                depth = max(depth, temp.first);
                st.push(pair<int, TreeNode*>(temp.first + 1, temp.second->left));
                st.push(pair<int, TreeNode*>(temp.first + 1, temp.second->right));
            }
        }
        return depth;
    }
};