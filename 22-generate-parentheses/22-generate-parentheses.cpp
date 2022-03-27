class Solution {
public:
    
    vector <string> result;
    
    void generate(string s, int left, int right)
    {
        if(left == 0 && right == 0)
            result.push_back(s);
        if(left > 0)
            generate(s + "(", left - 1, right);
        if(right > left)
            generate(s + ")", left, right - 1);
        
    }
    vector<string> generateParenthesis(int n) 
    {
        generate("", n, n);
        return result;
    }
};