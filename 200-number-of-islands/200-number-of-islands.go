func numIslands(grid [][]byte) int {
    
    result := 0
    
    for i, row := range grid {
        for j, value := range row {
            if value == '1' {
                dfs(&grid, i, j)
                result += 1
            }
        }
    }
    
    return result
    
}

func dfs(grid *[][] byte, r int, c int) {
    m, n := len(*grid), len((*grid)[0])
    if (r < 0) || (r >= m) || (c < 0) || (c >= n) || ((*grid)[r][c] == '0') {
        return
    }
       (*grid)[r][c] = '0'
       dfs(grid, r + 1, c)
       dfs(grid, r - 1, c)
       dfs(grid, r, c + 1)
       dfs(grid, r, c - 1)
}