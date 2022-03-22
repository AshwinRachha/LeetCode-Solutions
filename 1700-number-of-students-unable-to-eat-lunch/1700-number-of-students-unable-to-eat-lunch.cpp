class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) 
    {
        int num_students = students.size();
        int circle = 0; int square = 0;
        for(int i = 0; i < sandwiches.size(); i++)
        {
            if(students[i])
                square++;
            else
                circle++;
        }
        for(int i = 0; i < sandwiches.size();i++)
        {
            if(sandwiches[i] == 0)
            {
                if(circle > 0)
                {
                    num_students--; circle--;
                }
                else
                    return num_students;
            }
            else
            {
                if(square > 0)
                {
                    num_students--; square--;
                }
                else
                    return num_students;
            }
        }
        
        return num_students;
    }
};