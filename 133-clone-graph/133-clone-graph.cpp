/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    
    unordered_map <Node*, Node*> mp;
    
    Node* depthFirstSearch(Node* node)
    {
        if(node == NULL)
            return node;
        if(mp[node])
            return mp[node];
        Node* new_node = new Node(node->val);
        mp[node] = new_node;
        for(auto nei: node->neighbors){
            new_node->neighbors.push_back(cloneGraph(nei));
        }
        return new_node;
    }
    
    Node* cloneGraph(Node* node) 
    {
        return depthFirstSearch(node);
    }
};