class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_vector = defaultdict(int)
        for i, num in enumerate(nums):
            if num != 0:
                self.sparse_vector[i] = num
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        product = 0
        for i in self.sparse_vector:
            if i in vec.sparse_vector:
                product += self.sparse_vector[i] * vec.sparse_vector[i]
        return product
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)