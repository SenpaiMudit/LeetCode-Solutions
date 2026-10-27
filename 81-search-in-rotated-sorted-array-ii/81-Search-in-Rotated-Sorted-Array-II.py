class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        arr = list(set(nums))
        low= 0 
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == target:
                return True
            
            if arr[low] <= arr[mid]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return False
