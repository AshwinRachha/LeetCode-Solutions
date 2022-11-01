class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        rankMap = {}
        sorted_arr = sorted(arr)
        i = 0
        for num in sorted_arr:
            if num not in rankMap:
                rankMap[num] = i + 1
                i += 1
        ans = []
        for num in arr:
            ans.append(rankMap[num])
        return ans
        