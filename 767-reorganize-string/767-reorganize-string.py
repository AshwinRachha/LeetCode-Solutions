class Solution:
    def reorganizeString(self, s: str) -> str:
        
        c = Counter(s)
        ans = ['']*len(s)
        index = 0
        for k, v in c.most_common():
            for _ in range(v):
                if index == 0:
                    ans[index] = k
                    index +=2
                elif (0 < index < len(s) - 1) and (ans[index-1] == k or ans[index+1] == k):
                    return ""
                elif index == len(ans)and ans[index - 1] == k:
                    return ""
                else:
                    ans[index] = k
                    index += 2
                if index >= len(ans):
                    index = 1
        return "".join(ans)