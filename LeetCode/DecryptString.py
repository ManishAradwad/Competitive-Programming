def calc_alpha(n):
    return chr(int(n) + ord('a') - 1)
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i>=0:
            if s[i] == '#':
                res.append(calc_alpha(s[i-2:i]))
                i -= 3
            else:
                res.append(calc_alpha(s[i]))
                i -= 1
        res.reverse()
        return ''.join(res)