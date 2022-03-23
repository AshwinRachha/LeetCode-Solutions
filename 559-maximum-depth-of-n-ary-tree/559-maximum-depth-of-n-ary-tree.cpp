/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    int maxDepth(Node* root) 
    {
        if(root == NULL)
            return 0;
        else if(root->children.size() == 0)
            return 1;
        else
        {
            vector <int> heights;
            for(auto item : root->children)
            {
                heights.push_back(maxDepth(item));
            }
            return *max_element(heights.begin(), heights.end()) + 1;
        }
        
    }
};