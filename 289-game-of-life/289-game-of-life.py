class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        copy = [[board[row][col] for col in range(cols)] for row in range(rows)]
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        for row in range(rows):
            for col in range(cols):
                n = 0
                for nei in neighbors:
                    r = row + nei[0]
                    c = col + nei[1]
                    
                    if (r >=0 and r < rows) and (c < cols and c >= 0) and copy[r][c] == 1:
                        n += 1
                        
                if copy[row][col] == 1 and n < 2 or n > 3:
                    board[row][col] = 0
                if copy[row][col] == 0 and n == 3:
                    board[row][col] = 1
                    
                    
                        
                