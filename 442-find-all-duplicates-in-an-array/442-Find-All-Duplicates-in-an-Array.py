class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x = set()
        y = list()
        for i in nums:
            if i in x:
                y.append(i)
            else:
                x.add(i)
        return y
        