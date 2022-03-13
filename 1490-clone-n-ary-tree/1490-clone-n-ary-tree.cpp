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
        if(root == nullptr)
            return root;
        unordered_map <Node*, Node*> copy;
        deque <Node*> q;
        q.push_back(root);
        copy[root] = new Node(root->val);
        while(!q.empty())
        {
            Node* node = q.front(); q.pop_front();
            for(auto child : node->children)
            {
                copy[child] = new Node(child->val);
                copy[node]->children.push_back(copy[child]);
                q.push_back(child);
            }
        }
        
        return copy[root];
    }
};