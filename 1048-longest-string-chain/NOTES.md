words = set(words)
@lru_cache(maxsize = None)
def backtrack(word):
if word not in words:
return 0
maximum = 0
for i in range(len(word)):
maximum = max(maximum, backtrack(word[:i] + word[i+1:]) + 1)
return maximum
return max([backtrack(word) for word in words])