class Solution:
    def maximumSwap(self, num: int) -> int:
        original = list(str(num))
    
        rev_max = sorted(original, reverse=True)
    
        for i in range(len(original)):
            if original[i] < rev_max[i]:
                target_digit = rev_max[i]
            
                for j in range(len(original) - 1, i, -1):
                    if original[j] == target_digit:
                        original[i], original[j] = original[j], original[i]
                        return int("".join(original))
                    
        return num