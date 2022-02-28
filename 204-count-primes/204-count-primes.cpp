class Solution {
public:
    int countPrimes(int n) 
    {
       if(n == 0 || n == 1)
           return 0;
        vector <int> sieve(n, 1);
        sieve[0] = 0; sieve[1] = 0;
        for(int i = 0; i < sqrt(n); i++ )
        {
            if(sieve[i])
            {
                for(int j = i*i; j < n; j+=i)
                    sieve[j] = 0;
            }
        }
        
        return count(sieve.begin(), sieve.end(), 1);
    }
};