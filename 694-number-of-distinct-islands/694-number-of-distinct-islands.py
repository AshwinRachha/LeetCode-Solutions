class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c, direction):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 
            if (r, c) in seen:
                return
            seen.add((r,c))
            path_signature.append(direction)
            dfs(r + 1, c, "D")
            dfs(r - 1, c, "U")
            dfs(r, c - 1, "L")
            dfs(r, c + 1, "R")
            path_signature.append("0")
        
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path_signature = []
                dfs(row, col, "0")
                if path_signature:
                    unique_islands.add(tuple(path_signature))
        
        return len(unique_islands)