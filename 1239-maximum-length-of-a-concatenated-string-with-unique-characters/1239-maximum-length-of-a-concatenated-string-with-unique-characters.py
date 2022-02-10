class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        def backtrack(string, index):
            nonlocal max_len
            if len(set(string)) != len(string):
                return
            max_len = max(max_len, len(string))
            for i in range(index, len(arr)):
                backtrack(string + arr[i], i + 1)
        backtrack('', 0)    
        return max_len
