class Solution {
public:
    
    set <int> st;
    
    void dfs(set <int>& st, unordered_map <int, vector<int>>& graph, int node)
    {
        st.insert(node);
        for(auto child : graph[node])
        {
            if(st.find(child) == st.end())
            {
                st.insert(child);
                dfs(st, graph, child);
            }
        }
    }
    
    int makeConnected(int n, vector<vector<int>>& connections) 
    {
        if(connections.size() < n - 1)
            return -1;
        unordered_map <int, vector <int>> graph;
        for(auto v : connections)
        {
            graph[v[0]].push_back(v[1]);
            graph[v[1]].push_back(v[0]);
        }
        int count = 0;
        
        for(int i = 0; i < n; i++)
        {
            if(st.find(i)==st.end())
            {
                dfs(st, graph, i);
                count++;
            }
        }
        
        return count - 1;
    }
};