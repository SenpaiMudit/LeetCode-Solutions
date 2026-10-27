class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = nums[0]
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[low] <= nums[mid]:
                if nums[low] < minimum:
                    minimum = nums[low]
                low = mid + 1
            else:
                if nums[mid] < minimum:
                    minimum = nums[mid]
                high = mid - 1
                
        return minimum
