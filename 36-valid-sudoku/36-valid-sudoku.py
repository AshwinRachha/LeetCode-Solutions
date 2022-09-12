class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c] 
                if value == '.':
                    continue
                
                if value in rows[r]:
                    return False
                rows[r].add(value)
                
                if value in cols[c]:
                    return False
                cols[c].add(value)
                
                index = (r // 3) * 3 + (c // 3)
                if value in boxes[index]:
                    return False
                boxes[index].add(value)
        return True
                
        