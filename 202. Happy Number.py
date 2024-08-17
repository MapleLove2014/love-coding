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
    def isHappy2(self, n: int) -> bool:
        s = set()
        while n not in s:
            if n == 0:
                return False
            if n == 1 or (n % 10 == 0 and n // 10 == 0):
                return True
            s.add(n)
            ds = 0
            while n > 0:
                b = n % 10
                if b > 0:
                    ds += b ** 2
                n = n // 10
            n = ds
        return False
