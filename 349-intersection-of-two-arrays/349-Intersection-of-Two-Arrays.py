class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # did this so that nums 1 is smallest always
        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1
        look=set(nums2)
        seen=set()
        ans=[]
        for i in nums1:
            if (i in look and i not in seen):
                ans.append(i)
                seen.add(i)
        return ans
