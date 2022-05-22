class Solution {
public:
    
    int palindromicCount(string s, int left, int right)
    {
        int count = 0;
        while(left >= 0 && right < s.size() && s[left] == s[right])
        {
            left--;
            right++;
            count++;
        }
        return count;
    }
    
    int countSubstrings(string s) 
    {    
        int final_count = 0;
        
        for(int i = 0; i <= s.size(); i++)
        {
            int count1 = palindromicCount(s, i, i);
            int count2 = palindromicCount(s, i, i + 1);
            final_count += count1 + count2;
        }
        
        return final_count;
    }
};