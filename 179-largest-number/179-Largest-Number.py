class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums_str = [str(x) for x in nums]
        
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
                
            pivot = arr[len(arr) // 2]
            left, middle, right = [], [], []
            
            for x in arr:
                if x == pivot:
                    middle.append(x)
                elif x + pivot > pivot + x:
                    left.append(x)
                else:
                    right.append(x)
                    
            return quick_sort(left) + middle + quick_sort(right)

        sorted_strs = quick_sort(nums_str)
        result = "".join(sorted_strs)
        
        return "0" if result[0] == "0" else result
