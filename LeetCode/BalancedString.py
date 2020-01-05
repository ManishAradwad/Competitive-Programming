class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sub_str_count = 0
        bal_str_count = 0
        for i in range(1,len(s)+1):
            if s[i-1] == 'L':
                sub_str_count += 1
            else:
                sub_str_count -= 1
            if sub_str_count == 0:
                bal_str_count += 1
        return bal_str_count
            