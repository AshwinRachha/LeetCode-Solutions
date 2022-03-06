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
    Node* cloneTree(Node* root) 
    {
        if(root == NULL)
            return NULL;
        deque <Node*> que;
        unordered_map <Node*, Node*> mp;
        mp[root] = new Node(root->val);
        que.push_back(root);
        while(!que.empty())
        {
            Node* node = que.front(); que.pop_front();
            for(auto child : node->children)
            {
                mp[child] = new Node(child->val);
                que.push_back(child);
                mp[node]->children.push_back(mp[child]);
            }
        }
        
        return mp[root];
    }
};