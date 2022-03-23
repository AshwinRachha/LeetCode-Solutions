class Solution {
public:
    int minSteps(int n) 
    {
        int divisor = 2;
        int operations = 0;
        while(n > 1)
        {
            while(n % divisor == 0)
            {
                operations += divisor;
                n /= divisor;
            }
            divisor++;
        }
        return operations;
    }
};