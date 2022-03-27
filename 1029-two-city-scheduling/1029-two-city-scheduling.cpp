class Solution {
public:
    
    static bool customComparator(vector <int>& a, vector <int>& b)
    {
        return a[1] - a[0] > b[1] - b[0];
    }
    
    int twoCitySchedCost(vector<vector<int>>& costs) 
    {
        sort(costs.begin(), costs.end(), customComparator);
        int total_cost = 0;
        int n = 0;
        for(auto v : costs)
        {
            if(n >= costs.size() / 2)
            {
                total_cost += v[1];
            }
            else
            {
                total_cost += v[0];
                n++;
            }
        }
        return total_cost;
    }
};