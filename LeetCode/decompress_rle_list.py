# My soln
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        for i in range(int(len(nums)/2)):
            freq, val = nums[2*i], nums[2*i+1]
            for j in range(freq):
                result.append(val)
        return result