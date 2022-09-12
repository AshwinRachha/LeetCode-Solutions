class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        score = 0
        tokens.sort()
        ans = 0
        l, r = 0, len(tokens)-1
        while r >= l:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                ans = max(score, ans)
                l += 1
            elif score > 0:
                score -= 1
                power += tokens[r]
                r-=1
            else:
                return score
        return ans