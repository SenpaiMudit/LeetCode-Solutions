class Solution:
    def minSwapsCouples(self,row: list[int]) -> int:
        swaps = 0
        pos = {num: i for i, num in enumerate(row)}
    
        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = p1 ^ 1
        
            if row[i + 1] != p2:
                swaps += 1
                idx = pos[p2]
            
                wrong = row[i + 1]
                row[i + 1], row[idx] = row[idx], row[i + 1]
            
                pos[wrong] = idx
                pos[p2] = i + 1
            
        return swaps

        