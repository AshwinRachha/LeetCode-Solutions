class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        halved = n // 2
        c = Counter(arr)
        ans = 0
        for k, v in c.most_common():
            n-=v
            ans += 1
            if n <= halved:
                return ans
        return ans