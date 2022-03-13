class Solution {
public:
    int minNumberOperations(vector<int>& target) 
    {
        int changes = target[0];
        
        for(int i = 1; i < target.size();i++)
        {
            if(target[i] - target[i-1] > 0)
                changes += target[i] - target[i-1];
        }
        
        return changes;
    }
};