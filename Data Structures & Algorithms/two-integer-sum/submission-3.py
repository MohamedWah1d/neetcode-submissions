class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resD = defaultdict(int)
        for i, n in enumerate(nums):
            sub = target - n
            if n in resD:
                return [resD[n], i]  

            resD[sub] = i