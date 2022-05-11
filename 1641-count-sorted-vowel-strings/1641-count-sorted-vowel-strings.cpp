class Solution {
public:
    
    vector <char> vowels = {'a', 'e', 'i', 'o', 'u'};
    
    void backtrack(int n, char last, int &count)
    {
        if(n == 0)
        {
            count++;
            return;
        }
        else
        {
            for(auto e : vowels)
                if(last <= e)
                    backtrack(n-1, e, count);
        }
    }
    
    int countVowelStrings(int n) 
    {
        int count = 0;
        backtrack(n, ' ', count);
        return count;
    }
};