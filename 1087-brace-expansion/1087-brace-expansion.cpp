class Solution {
public:
    
    vector <vector<char>> allOptions;
    
    void storeAllOptions(string& s)
    {
        for(int pos = 0; pos < s.size(); pos++)
        {
            vector <char> currOptions;
            if(s[pos] != '{')
            {
                currOptions.push_back(s[pos]);
            }
            else
            {
                while(s[pos]!='}')
                {
                    if(s[pos] >= 'a' && s[pos] <= 'z')
                    {
                        currOptions.push_back(s[pos]);
                    }
                    pos++;
                }
                sort(currOptions.begin(), currOptions.end());
            }
            allOptions.push_back(currOptions);
        }
    }
    
    void generateWords(string currString, vector <string>& expandedWords)
    {
        if(currString.size() == allOptions.size())
        {
            expandedWords.push_back(currString);
            return;
        }
        vector <char> currOptions = allOptions[currString.size()];
        for(char c : currOptions)
        {
            currString += c;
            generateWords(currString, expandedWords);
            currString.pop_back();
        }
    }
    
    vector<string> expand(string s) 
    {
        storeAllOptions(s);
        vector <string> expandedWords;
        generateWords("", expandedWords);
        return expandedWords;
    }
};