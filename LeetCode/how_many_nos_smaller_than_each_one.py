# My soln
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = []
        for i in nums:
            count = 0
            for j in nums:
                if j != i and j < i:
                    count += 1
            counts.append(count)
        return counts

# Best soln
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        count, temp = 0, {}
        for num in sorted(freq.keys()):
            temp[num] = count
            count += freq[num]
        return [temp[i] for i in nums]