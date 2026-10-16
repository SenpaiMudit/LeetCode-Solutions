import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        answers=[1]*n
        prefix = 1
        for i in range(n):
            answers[i]= prefix
            prefix *= nums[i]
        sufix=1
        for i in range(n-1,-1,-1):
            answers[i]*=sufix
            sufix*=nums[i]
        return answers