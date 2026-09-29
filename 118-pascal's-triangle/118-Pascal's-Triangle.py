class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Initialize the outer array to hold all rows
        triangle = []
        
        for i in range(numRows):
            # 1. Create a row with an increasing length of (i + 1)
            row = [None] * (i + 1)
            
            # 2. Fill the first and last elements as 1
            row[0] = 1
            row[-1] = 1
            
            # 3. Sum the remaining inner numbers from the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            # Append the completed row to our main triangle array
            triangle.append(row)
            
        return triangle
