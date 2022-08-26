class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        dic = {}
        for region in regions:
            for r in region[1:]:
                dic[r] = region[0]
        seen = set()
        seen.add(region1)
        while region1 in dic:
            seen.add(dic[region1])
            region1 = dic[region1]
        while region2 not in seen:
            region2 = dic[region2]
        return region2
        
        