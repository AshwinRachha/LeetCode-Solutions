class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols  = len(board), len(board[0])
        visited = set()
        def backtrack(index, r, c):
            if r < 0 or c < 0 or  c >= cols or r >= rows or (r,c) in visited:
                return False
            if board[r][c] != word[index]:
                return False
            if index == len(word)-1:
                return True
            visited.add((r, c))
            one = backtrack(index + 1, r+1, c)
            two = backtrack(index + 1, r-1, c)
            three = backtrack(index + 1, r, c+1)
            four = backtrack(index + 1, r, c-1)
            visited.remove((r, c))
            return one or two or three or four
        
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(0, i, j):
                        return True
        return False