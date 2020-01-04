class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(x) for x in str(n)]
        add = sum(n)
        produ = 1
        for i in n:
            produ *= i
        return produ-add