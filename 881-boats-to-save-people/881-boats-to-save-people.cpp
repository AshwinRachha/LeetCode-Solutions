class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) 
    {
        sort(people.begin(), people.end());
        int num_boats = 0;
        int left = 0; int right = people.size() - 1;
        while(left <= right)
        {
            num_boats++;
            if(people[left] + people[right] <= limit)
                left++;
            right--;
        }
        return num_boats;
    }
};