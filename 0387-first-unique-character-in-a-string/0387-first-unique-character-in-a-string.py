class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        arr = [0] * 26
        
        for c in s:
            arr[ord(c) - ord('a')] += 1
        for i, c in enumerate(s):
            if arr[ord(c) - ord('a')] == 1:
                return i
        return -1