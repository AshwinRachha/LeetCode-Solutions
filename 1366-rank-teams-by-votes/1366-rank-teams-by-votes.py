class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        d = dict()
        for vote in votes:
            for i, c in enumerate(vote):
                if c not in d:
                    d[c] = [0] * len(vote)
                d[c][i] += 1
        sorted_names = sorted(d.keys())
        voted_names = sorted(d.keys())
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))
        
        