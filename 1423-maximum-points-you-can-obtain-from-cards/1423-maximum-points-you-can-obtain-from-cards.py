class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        1 2 3 4 5 6 1 -> s = 22, n = 7, k = 3
        """
        
        totalSum, n = sum(cardPoints), len(cardPoints)
        # We have to take all cards so return sum of array
        if n == k:
            return totalSum
        # else, we have a choice to include either 1st element, 1st and 2nd element,
        # 1...k elements from the front, or we can take the last element, to n - k from the end
        # or we can take k elements from the beginning and the end. 
        
        # For this purpose we need a sliding window across the array and we will pick out 
        # the max out of them
        currentWindowSum = sum(cardPoints[:n-k])
        ans = currentWindowSum
        for i in range(n-k, n):
            currentWindowSum -= cardPoints[i - (n - k)]
            currentWindowSum += cardPoints[i]
            ans = min(ans, currentWindowSum)
        return totalSum - ans
            