from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_element = min(nums)
        summ = 0  # Changed 'sum' to 'total_moves'
        
        for i in nums:
            min_diff = abs(i - min_element)
            summ += min_diff
            
        return summ
