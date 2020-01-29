"""
Desciption: Given a sequence of brackets, calculate the score.
"""

# 
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[]
        score=0
        for bracket in S:
            if bracket=='(':
                stack.append(score)
                score=0
            else:
                score = stack.pop() + max(score*2,1)
        return score