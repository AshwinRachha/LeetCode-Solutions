class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        self.ans = 0
        m, n = len(picture), len(picture[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] =='B':
                    rows[i] += 1
                    cols[j] += 1           
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    self.ans += 1
        return self.ans
    