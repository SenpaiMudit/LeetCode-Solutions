class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        l1=[]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    l1.append((r,c))
        
        for r,c in l1:
            for i in range(cols):
                matrix[r][i]=0
            for j in range(rows):
                matrix[j][c]=0

        