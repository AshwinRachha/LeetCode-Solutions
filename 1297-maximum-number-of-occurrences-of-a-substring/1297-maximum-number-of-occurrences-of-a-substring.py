class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        count = Counter()
        n = len(s)
        for i in range(n - minSize + 1):
            sub_str = s[i:i  + minSize]
            if len(set(sub_str)) <= maxLetters:
                count[sub_str] += 1
        return max(count.values()) if count else 0