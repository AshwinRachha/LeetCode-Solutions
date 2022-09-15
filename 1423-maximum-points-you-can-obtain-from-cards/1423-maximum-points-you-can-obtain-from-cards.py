class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        1 2 3 4 5 6 1 -> s = 22, n = 7, k = 3
        """
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
            