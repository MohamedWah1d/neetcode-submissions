class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while r > l:
                if nums[i] + nums[l] + nums[r] == 0:
                    out.add((nums[i], nums[l], nums[r]))
                    r -=1
                    l +=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -=1
                else:
                    l += 1

        return [list(t) for t in out]
            