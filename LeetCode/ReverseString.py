"""
Given an array of characters s, reverse all the characters.
"""
# One word solution----
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
    
# Recursive Solution----
#    Time Complexity- O(N) to perform N/2 swaps
#    Space Complexity- O(N) to keep the recursion stack
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left,right):
            if left < right:
                s[left],s[right] = s[right],s[left]
                helper(left + 1, right - 1)
        helper(0,len(s)-1)

# Two Pointer's approach----
#    Time Complexity- O(N) for N/2 swaps
#    Space Complexity- O(1), constant space solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while(left<=right):
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1