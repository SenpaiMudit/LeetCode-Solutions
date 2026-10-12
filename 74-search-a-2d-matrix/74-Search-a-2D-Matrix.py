class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bottom = rows - 1
        target_row = -1
        
        while top <= bottom:
            mid_row = (top + bottom) // 2
            
            if matrix[mid_row][0] <= target <= matrix[mid_row][cols - 1]:
                target_row = mid_row
                break
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                top = mid_row + 1
                
        if target_row == -1:
            return False
            
        left = 0
        right = cols - 1
        
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[target_row][mid_col] == target:
                return True
            elif matrix[target_row][mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1
                
        return False
