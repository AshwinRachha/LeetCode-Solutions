class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        def backtrack(index, path):
            nonlocal max_len
            if index >= len(arr):
                if len(set(path)) == len(path):
                    max_len = max(max_len, len(path))
                return
            backtrack(index + 1, path + arr[index])
            backtrack(index + 1, path)
        
        backtrack(0, "")
        return max_len