class Solution {
public:
    int compress(vector<char>& chars) 
    {
        int i = 0, index = 0;
        while(i < chars.size())
        {
            int j = i;
            while(j < chars.size() && chars[j] == chars[i])
                    j++;
            
            chars[index++] = chars[i];
            if(j - i > 1)
            {
                for(auto s : to_string(j-i))
                    chars[index++] = s;
            }
            
            i = j;
        }
        return index;
    }
    
    
};