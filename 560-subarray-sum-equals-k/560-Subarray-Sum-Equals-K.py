class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        summ=0
        count=0
        for i in nums:
            summ+=i
            if summ-k in seen:
                count+=seen[summ-k]
            seen[summ]=seen.get(summ,0)+1
        return count
            