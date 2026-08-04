class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (n + nums[l] + nums[r] == 0):
                    res.add((n, nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif (n + nums[l] + nums[r] > 0):
                    r -= 1
                else:
                    l += 1
        return [list(t) for t in res] 