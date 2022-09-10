class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def dfs(r, c, first):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if board[r][c] != 'O':
                return
            if first:
                board[r][c] = '#'
            else:
                board[r][c] = 'X'
            dfs(r + 1, c, first)
            dfs(r - 1, c, first)
            dfs(r, c + 1, first)
            dfs(r, c - 1, first)
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == 'O':
                    dfs(r, c, first = True)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    dfs(r,c, first = False)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
        