class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num_set = set(nums)
        i = 1
        while True:
            if i not in num_set:
                return i            
            i += 1