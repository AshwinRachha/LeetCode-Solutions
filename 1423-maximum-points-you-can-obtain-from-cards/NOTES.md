totalSum = sum(cardPoints)
n = len(cardPoints)
if k == n:
return totalSum
currentWindowSum = sum(cardPoints[:n-k])
ans = currentWindowSum
for i in range(n-k, n):
currentWindowSum -= cardPoints[i-(n-k)]
currentWindowSum += cardPoints[i]
ans = min(ans, currentWindowSum)
return totalSum - ans