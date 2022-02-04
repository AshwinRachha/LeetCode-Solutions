class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        ans = ''
        
        dic = {}
        for v1, v2 in knowledge:
            dic[v1] = v2
        i = 0; n = len(s)
        while i < n:
            if s[i] == '(':
                key = ''; i+=1
                while i < len(s) and s[i]!=')':
                    key += s[i]
                    i+=1
                if key in dic:
                    ans += dic[key]
                else:
                    ans+='?'
            else:
                ans+=s[i]
            i+=1
        return ans