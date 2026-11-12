class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_or_equal(x: int) -> int:
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        low, high = 1, m * n
        while low < high:
            mid = low + (high - low) // 2
            if count_less_or_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low
