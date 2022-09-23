class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        string = ""
        MOD = 10 ** 9 + 7
        for i in range(1, n + 1):
            string += bin(i)[2:]
        return int(string, 2) % MOD
        