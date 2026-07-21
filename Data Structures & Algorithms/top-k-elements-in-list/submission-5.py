class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Bucket sort way

        countDict = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)] # so if we have  [1, 1] we will make an array of 0,1 but we need 2 as well.

        for n in nums:
            countDict[n] += 1

        res = []
        for n, c in countDict.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        
