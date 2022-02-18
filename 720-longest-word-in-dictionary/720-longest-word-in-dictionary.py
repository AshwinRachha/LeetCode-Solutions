class Solution:
    def longestWord(self, words: List[str]) -> str:
        seen = set(words)
        words.sort()
        max_word = ""
        for word in words:
            boolean = True
            for i in range(len(word)):
                prefix = word[:i+1]
                if prefix not in seen:
                    boolean = False
                    break
            if boolean:
                if max_word is None or len(max_word) < len(word):
                    max_word = word
        return max_word
        