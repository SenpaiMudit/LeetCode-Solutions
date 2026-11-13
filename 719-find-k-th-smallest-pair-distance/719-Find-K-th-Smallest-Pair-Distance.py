class Solution:
  def smallestDistancePair(self, nums: list[int], k: int) -> int:
    nums.sort()

    def count_pairs_with_distance_at_most(max_distance: int) -> int:
      count = 0
      left = 0
      for right in range(len(nums)):
        while nums[right] - nums[left] > max_distance:
          left += 1
        count += right - left
      return count

    low = 0
    high = nums[-1] - nums[0]

    while low < high:
      mid = (low + high) // 2
      if count_pairs_with_distance_at_most(mid) >= k:
        high = mid
      else:
        low = mid + 1

    return low
