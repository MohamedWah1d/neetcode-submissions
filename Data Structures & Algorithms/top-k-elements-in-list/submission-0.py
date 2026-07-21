class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]
        
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
        
        vals = sorted(res, key=res.get, reverse=True)

        return vals[:k]
        