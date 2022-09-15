class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        dic = defaultdict(int)
        start, end = 0, 0
        max_len = 0
        for end, c in enumerate(s):
            dic[c] = end
            if len(dic) > k:
                start = min(dic.values())
                del dic[s[start]]
                start = start + 1 
            max_len = max(max_len, end - start + 1)
        return max_len