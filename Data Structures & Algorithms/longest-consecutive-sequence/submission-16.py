class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        c = 1
        longest = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1] - 1 :
                c += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                c = 1
            longest = max(c, longest)
        
        return longest