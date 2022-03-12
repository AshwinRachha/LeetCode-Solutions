class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1) + dfs(r, c+1)
         
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and grid[r][c] == 1:
                    dfs(r,c)
        return sum(sum(row) for row in grid)