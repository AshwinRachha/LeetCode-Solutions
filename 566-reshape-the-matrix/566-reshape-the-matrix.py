class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        x, y = len(mat), len(mat[0])
        if(x == 0 or r*c != x*y):
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]
        q = deque()
        for i in range(x):
            for j in range(y):
                q.append(mat[i][j])
        
        for i in range(r):
            for j in range(c):
                ans[i][j] = q.popleft()
        return ans