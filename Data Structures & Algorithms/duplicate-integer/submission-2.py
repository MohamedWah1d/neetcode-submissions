class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        comparison = set(nums)
        if len(nums) == len(comparison):
            return False
        else:
            return True
