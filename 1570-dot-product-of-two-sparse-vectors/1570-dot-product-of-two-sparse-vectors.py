class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.dic = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.dic[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        res = 0
        for i, n in self.dic.items():
            if i in vec.dic:
                res += n * vec.dic[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)