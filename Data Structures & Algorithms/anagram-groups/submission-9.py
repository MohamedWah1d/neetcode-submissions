class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # The idea here is to have a dict of lists as the final result
        # the key here will be the combination of the count of each character
        # inside each string inside the strs, and the value will be the anagrams.

        if len(strs) <= 1:
            return [strs]
        
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            
            res[tuple(count)].append(s)
        return list(res.values())