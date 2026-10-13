class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        max_count = 0
        count=1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1 
                
        return max(max_count, count)
