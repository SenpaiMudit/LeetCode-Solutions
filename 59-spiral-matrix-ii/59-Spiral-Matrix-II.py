class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while top <= bottom and left <= right: # limits taaki out of bound na ho
            for i in range(left, right + 1): #moving right
                matrix[top][i] = num
                num += 1
            top += 1 #updating so that we dont go in that same row 
            
            for i in range(top, bottom + 1): #moving down
                matrix[i][right] = num
                num += 1
            right -= 1 #updating so that we dont go in that same column
            
            for i in range(right, left - 1, -1): #left
                matrix[bottom][i] = num
                num += 1
            bottom -= 1 #updating so that we dont go in that same row 
            
            for i in range(bottom, top - 1, -1): # up
                matrix[i][left] = num
                num += 1 #updating so that we dont go in that same coolumn 
            left += 1
            
        return matrix
