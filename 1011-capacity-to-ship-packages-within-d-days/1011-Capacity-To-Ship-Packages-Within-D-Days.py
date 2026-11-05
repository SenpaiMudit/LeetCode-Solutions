class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            days_needed = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    days_needed += 1
                    current_weight = 0
                current_weight += w
            return days_needed <= days

        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1  
                
        return left
