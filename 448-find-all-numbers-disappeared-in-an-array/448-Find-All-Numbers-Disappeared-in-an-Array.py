class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        n = len(nums)
        nums.sort()
        missing = []
        
        for missing_num in range(1, nums[0]):
            missing.append(missing_num)
            
        for i in range(len(nums) - 1):
            current = nums[i]
            nxt = nums[i + 1]
            
            if current == nxt:
                continue
                
            if current + 1 != nxt:
                for missing_num in range(current + 1, nxt):
                    missing.append(missing_num)
                    
        if nums[-1] < n:
            for missing_num in range(nums[-1] + 1, n + 1):
                missing.append(missing_num)
                
        return missing
