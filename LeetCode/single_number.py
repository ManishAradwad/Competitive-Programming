class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)
        for key,value in counts.items():
            if value==1:
                return key


