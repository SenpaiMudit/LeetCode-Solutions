class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        x=sorted(nums)
        n=len(nums)
        i=(n-1)//2
        j=n-1
        for m in range(n):
            if(m%2==0):
                nums[m]=x[i]
                i=i-1
            else:
                nums[m]=x[j]
                j=j-1

        