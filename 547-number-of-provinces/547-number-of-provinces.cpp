class Solution {
public:
    
    void depthFirstSearch(int i, set <int>& st, unordered_map <int, vector<int>>& graph, vector<vector<int>>& isConnected)
    {
        vector <int> edges = graph[i];
        st.insert(i);
        for(auto j : edges)
        {
            if(st.find(j)==st.end() && isConnected[i][j])
                depthFirstSearch(j, st, graph, isConnected);
        }
    }
    
    int findCircleNum(vector<vector<int>>& isConnected) 
    {
        int n = isConnected.size();
        set <int> st;
        unordered_map <int, vector<int>> graph;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(isConnected[i][j])
                    graph[i].push_back(j);
            }
        }
        int count = 0;
        for(int i = 0; i < n; i ++)
        {
           if(st.find(i)==st.end())
           {
               depthFirstSearch(i, st, graph, isConnected);
               count++;
           }
        }
        return count;
        
    }
};