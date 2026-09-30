class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Initialize the outer array to hold all rows up to rowIndex
        triangle = []
        
        # We need to generate up to rowIndex + 1 rows
        for i in range(rowIndex + 1):
            # 1. Create a row with an increasing length of (i + 1)
            row = [None] * (i + 1)
            
            # 2. Fill the first and last elements as 1
            row[0] = 1
            row[-1] = 1
            
            # 3. Sum the remaining inner numbers from the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
            # same as pascal triangle 1 (119 leetcode)
        return triangle[rowIndex] #instead of printing whole triangle we only print the last row
