self.count = 0
seen = set()
def backtrack(index):
if index > n:
self.count+=1
for i in range(1, n+1):
if i not in seen and (i % index == 0 or index % i == 0):
seen.add(i)
backtrack(index + 1)
seen.remove(i)
backtrack(1)
return self.count