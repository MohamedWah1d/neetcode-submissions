class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resCounter = defaultdict(int)
        for n in nums:
            resCounter[n] += 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in resCounter.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)
        
        return res
