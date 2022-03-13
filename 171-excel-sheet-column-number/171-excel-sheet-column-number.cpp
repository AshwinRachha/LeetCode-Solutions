class Solution {
public:
    int titleToNumber(string columnTitle) 
    {
        int result = 0;
        int power = columnTitle.size() - 1;
        for(auto c : columnTitle)
        {
            int mult = c -'A' + 1;
            result += pow(26, power) * mult;
            power--;
        }
        return result;
    }
};