class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        count = 0

        def summ(index, sun):
            nonlocal count
            if index == n:
                if sun == target:
                    count += 1
                return
            
            summ(index + 1, sun + nums[index])
            summ(index + 1, sun - nums[index])

        summ(0, 0)
        return count
