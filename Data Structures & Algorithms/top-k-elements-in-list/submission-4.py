class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Here we have the target which is k, we will do a dict and count
        # They keys which are the values of the array how many time they
        # appeared on the list, and at the end return only any nuber that is 
        # Greater than k.

        countDict = defaultdict(int)
        for n in nums:
            countDict[n] +=1

        res = sorted(countDict, key=countDict.get, reverse=True)

        return res[:k]
