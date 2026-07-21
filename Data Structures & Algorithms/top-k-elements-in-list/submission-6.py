class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resCounter = defaultdict(int)
        for n in nums:
            resCounter[n] += 1
        
        res = sorted(resCounter, key=resCounter.get, reverse=True)

        return res[:k]