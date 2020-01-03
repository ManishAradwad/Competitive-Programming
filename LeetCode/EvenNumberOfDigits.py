class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            digits = 0
            while(x>=0):
                digits += 1
                x %= 10
            if digits % 2 == 0:
                ans += 1
        return ans