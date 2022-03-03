class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) 
    {
        int ans = 0;
        
        for(int i = homePos[0]; i != startPos[0]; i += i > startPos[0] ? -1 : 1)
        {
            ans += rowCosts[i];
        }
        
        for(int j = homePos[1]; j != startPos[1]; j += j > startPos[1] ? -1 : 1)
        {
            ans += colCosts[j];
        }
        return ans;
    }
};