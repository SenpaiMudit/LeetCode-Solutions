class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        m= len(matrix)
        n = len(matrix[0])
        low = matrix[0][0]
        high = matrix[m-1][n-1]
        
        def countLessOrEqual(mid):
            count = 0
            c = n - 1 
            for r in range(m):
                while c >= 0 and matrix[r][c] > mid:
                    c -= 1
                count += (c + 1)
            return count

        while low < high:
            mid = low + (high - low) // 2
            if countLessOrEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low
