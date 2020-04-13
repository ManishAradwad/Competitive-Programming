class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = min(nums)
        a = 0
        for i in nums:
            a += i
            largest_sum = max(largest_sum, a)
            a = max(0, a)
        return (largest_sum)
