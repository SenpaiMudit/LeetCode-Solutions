import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        max_m = int(math.log2(num))
        
        for m in range(max_m, 1, -1):
            k = int(num ** (1 / m))
            if (k ** (m + 1) - 1) // (k - 1) == num:
                return str(k)
                
        return str(num - 1)
