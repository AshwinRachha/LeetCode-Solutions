class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters = [l for l in logs if l.split()[1].isalpha()]
        digits = [d for d in logs if d.split()[1].isdigit()]
        letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return letters + digits
        