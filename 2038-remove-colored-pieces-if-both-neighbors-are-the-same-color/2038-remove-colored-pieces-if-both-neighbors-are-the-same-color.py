class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        A_count, B_count = 0, 0
        a, b = 0, 0
        for c in colors:
            if c == 'A':
                A_count+=1
                if A_count > 2:
                    a+=1
                B_count = 0
            else:
                B_count += 1
                if B_count > 2:
                    b+=1
                A_count = 0
        return a > b