class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubsequence(s, word):
            m, n = len(s), len(word)
            i, j = 0, 0
            while i < m and j < n:
                if s[i] == word[j]:
                    j+=1
                i+=1
            return j == n
        result = ''
        dictionary.sort()
        for word in dictionary:
            if len(word) > len(s):
                continue
            if isSubsequence(s, word) and len(word) > len(result):
                result = word
        return result