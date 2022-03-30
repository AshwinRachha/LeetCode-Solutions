class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) 
    {
     
        int rows = matrix.size();
        int columns = matrix[0].size();
        int m = 0, n = columns - 1;
    
        while (m < rows && n >= 0)
        {
            int start = matrix[m][n];
            if(start == target) return true;
            else if(start > target) n--;
            else m++;
        }
        return false;
        
    }
};