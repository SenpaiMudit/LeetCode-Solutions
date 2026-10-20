from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
            
        q = deque()
        x = []
        
        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()
                
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
                
            q.append(i)
            
            if i >= k - 1:
                x.append(nums[q[0]])
                
        return x
