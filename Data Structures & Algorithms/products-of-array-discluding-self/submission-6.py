class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prefix = 1
        postfix = 1

        for i in range(len(nums )):
            out.append(prefix)
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            out[i] *= postfix
            postfix *= nums[i]

        return out
            