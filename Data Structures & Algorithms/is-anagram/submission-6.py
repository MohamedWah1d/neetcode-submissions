class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dS = defaultdict(int)
        dT = defaultdict(int)
        for ns, nt in zip(s, t):
            dS[ns] += 1
            dT[nt] += 1
        for nt in t:
            if dS[nt] != dT[nt]:
                return False
        return True
