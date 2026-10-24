class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 4:
            return num == 1
            
        low = 2
        high = num // 2
        
        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square > num:
                high = mid - 1
            else:
                low = mid + 1
                
        return False
