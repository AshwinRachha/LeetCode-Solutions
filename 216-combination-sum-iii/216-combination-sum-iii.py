class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        seen = set()
        output = []
        def backtrack(number, s, array):
            if len(array) == k and s == n:
                output.append(array[:])
                return
            if len(array) >= k and s != n:
                return
            number = 0 if not array else array[-1]
            for i in range(number + 1,10):
                backtrack(number, s + i, array + [i])
        backtrack(1, 0, [])
        return output