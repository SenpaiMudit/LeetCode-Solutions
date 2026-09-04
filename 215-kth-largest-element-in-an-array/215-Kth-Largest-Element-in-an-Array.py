class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        sorted_nums = sorted(counts.keys(), reverse=True)
    
        seen = 0
        for num in sorted_nums:
            seen += counts[num]
            if seen >= k:
                return num    