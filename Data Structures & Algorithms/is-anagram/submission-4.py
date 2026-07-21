class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we will have to make a dict > this dict will hold the values of each of 
        # the strings, and then we will count each character on each one and save it
        # as a value for this key, they keys are the chars, then we compare the two
        # dicts on each similar key, do they have the same count or no.

        if len(s) != len(t):
            return False

        countS, countT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1 
            countT[t[i]] += 1

        for  cs in s:
            if countS[cs] != countT[cs]:
                return False

        return True 
        
