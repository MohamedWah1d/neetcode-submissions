class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The idea here is to have a dict where we will save on it the difference
        # the target and the real value as the key and the value is the key, and
        # then we loop and ask does this new value on the array already exists on
        # the dict or no, if yes then this old value of the key and this index are 
        # answers.
        res = defaultdict(int)

        for i, n in enumerate(nums):
            sub = target - n

            if n in res:
                return [res[n], i]
            
            res[sub] = i