class Solution {
public:
    
    int max_len = 0;
    
    int maxLength(vector<string>& arr) 
    {
        backtrack("", arr, 0);
        return max_len;
    }
    
    void backtrack(string str, vector <string> &arr, int index)
    {
        if(!isUnique(str)) return;
        if(str.size() > max_len) max_len = str.size();
        for(int i = index; i < arr.size(); i++)
            backtrack(str + arr[i], arr, i+1);
    }
    
    bool isUnique(string str)
    {
        set <char> st;
        for(auto l : str)
        {
            if(st.find(l)!= st.end())
                return false;
            st.insert(l);
        }
        return true;
    }
    
};