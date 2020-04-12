class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        def square_maker(number):
            result = 0
            while(number):
                result += (number%10) * (number%10)
                number = int(number/10)
            return result
        
        
        while(True):
            slow = square_maker(slow)
            fast = square_maker(square_maker(fast))
            if slow != fast:
                continue
            else:
                break
        return (slow==1)
     
            
