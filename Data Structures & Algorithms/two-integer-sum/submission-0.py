class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrayVal = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in arrayVal:
                return [arrayVal[diff], i]
            arrayVal[n] = i