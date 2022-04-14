class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    value = board[i][j]
                    rows[i].add(value)
                    cols[j].add(value)
                    boxes[i//3][j//3].add(value)
        
        def backtrack(i, j):
            if i == len(board):
                return True
            elif j == len(board[i]):
                return backtrack(i+1, 0)
            elif board[i][j] != ".":
                return backtrack(i, j+1)
            else:
                for num in range(1, 10):
                    value = str(num)
                    if((value not in rows[i]) and (value not in cols[j]) and (value not in boxes[i//3][j//3])):
                        rows[i].add(value)
                        cols[j].add(value)
                        boxes[i//3][j//3].add(value)
                        board[i][j] = value
                        if backtrack(i, j+1):
                            return True
                        else:
                            board[i][j] = "."
                            rows[i].remove(value)
                            cols[j].remove(value)
                            boxes[i//3][j//3].remove(value)
            return False
        
        backtrack(0, 0)