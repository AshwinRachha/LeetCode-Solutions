class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(cols):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1, rows):
            for j in range(1, cols):
                
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
        