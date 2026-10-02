class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #to solve this in linear time complexity and constant space we must use voting system
        temp=None
        count=0
        for i in nums:
            if count==0:
                temp=i
            if temp==i:
                count+=1
            else:
                count-=1
        return temp