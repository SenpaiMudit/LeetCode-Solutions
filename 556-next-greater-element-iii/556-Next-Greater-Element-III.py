class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=list(str(n))
        k= len(nums)
        i = k- 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = k- 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        left, right = i + 1, k- 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        number=int("".join(nums))
        if number>2147483647:
            return -1
        if(number>n):
            return number
        else:
            return -1