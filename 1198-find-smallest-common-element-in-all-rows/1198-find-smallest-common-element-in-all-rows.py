class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        
        """
        1 2 3 4 5
        2 4 5 8 10
        3 5 7 9 11
        1 3 5 7 9
        """
        
        frequencies = Counter()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                frequencies[mat[i][j]] += 1
        for k, v in frequencies.items():
            print(v, n)
            if v == m:
                return k
        return -1
        
        