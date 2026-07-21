class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The idea is to use prefix and postfix, and solve it on the output array
        # so for example let's take this [1,2,4,6] , the prefix of 1 is 1, and the 
        # prefix of 4 is 8 and will be placed on the 4th position because when we 
        # multiply the postfix we need to have it on the right place!
        # and so on for the postfix

        prefix, postfix = 1, 1
        out = []

        for n in nums:
            out.append(prefix)
            prefix *= n

        for i in range(len(nums)-1, -1, -1):
            out[i] *= postfix
            postfix *= nums[i]

        return out
            
            