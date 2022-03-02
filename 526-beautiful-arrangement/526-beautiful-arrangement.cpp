class Solution {
public:
    
    int count = 0;
    set <int> st;
    void backtrack(int index,int n)
    {
        if(index > n)
        {
            count++;
            return;
        }
        for(int i = 1; i < n + 1; i++)
        {
            if(st.find(i) == st.end() && (i % index == 0 || index % i == 0))
            {
                st.insert(i);
                backtrack(index + 1, n);
                st.erase(i);
            }
        }
        
    }
    
    int countArrangement(int n) 
    {
        backtrack(1, n);
        return count;
    }
    
};