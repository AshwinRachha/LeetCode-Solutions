class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        start, end = 0, 0
        dic = defaultdict(int)
        for end, c in enumerate(s):
            if c in dic:
                start = max(start, dic[c])
            max_len = max(max_len, end - start+1)
            dic[c] = end + 1
        
        return max_len
    
        """
        a : 0
        b : 1
        c : 2
        """