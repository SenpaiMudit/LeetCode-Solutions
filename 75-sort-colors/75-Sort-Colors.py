class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[0,1,2]
        count=[0]*3
        n=len(nums)
        for i in arr:
            count[i]=nums.count(i)
        for i in range(n):
            if count[0]>0:
                nums[i]=arr[0]
                count[0]-=1
            elif count[1]>0:
                nums[i]=arr[1]
                count[1]-=1
            elif count[2]>0:
                nums[i]=arr[2]
                count[2]-=1

    
        