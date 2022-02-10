class Solution {
public:
    string toLowerCase(string s) 
    {        
        for(int i = 0; i < s.size();i++)
        {
            if( (int)s[i] >= (int)'A' && (int)s[i] <= (int)'Z')
            {
                s[i] = (char)(97 + ((int)s[i]) - (int)'A' );
            }
        }
        return s;
    }
};