class Solution:
    def isHappy(self, n: int) -> bool:
        l = set()
        while True:
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n = n // 10
            if s == 1:
                return True
            if s in l:
                return False
            n = s
            l.add(n)
