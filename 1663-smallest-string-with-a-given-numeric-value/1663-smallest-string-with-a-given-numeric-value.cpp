class Solution {
public:
    string getSmallestString(int n, int k) 
    {
        string ans(n, 'a');
        k -= n;
        for(int position = n - 1; position >= 0 && k > 0; position--)
        {
            int add = min(k, 25);
            ans[position] = (char)(ans[position] + add);
            k -= add;
        }
        return ans;
    }
};