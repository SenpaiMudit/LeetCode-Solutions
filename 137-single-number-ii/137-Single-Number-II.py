class Solution:
    def singleNumber(self,nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
    
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        for i in range(1, len(nums) - 1):
            prev_val = nums[i - 1]
            curr_val = nums[i]
            next_val = nums[i + 1]
        
            if curr_val != prev_val and curr_val != next_val:
                return curr_val
