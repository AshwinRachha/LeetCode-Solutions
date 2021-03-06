class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> q;
    int k1;
    KthLargest(int k, vector<int>& nums) 
    {
        k1 = k;
        for(auto num : nums)
        {
            q.push(num);
        }
        while(q.size() > k)
            q.pop();
    }
    
    int add(int val) 
    {
        q.push(val);
        if(q.size() > k1)
            q.pop();
        return q.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */