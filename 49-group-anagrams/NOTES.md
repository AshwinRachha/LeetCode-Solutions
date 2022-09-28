class Solution:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
dic = defaultdict(list)
for s in strs:
key = "".join(sorted(s))
dic[key].append(s)
return [val for _, val in dic.items()]