class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        left = abs(dividend)
        times = 0
        if dividend == 0:
            return 0
        pos = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        if abs(divisor) == 1:
            return abs(dividend) if pos else -abs(dividend)


        while left >= abs(divisor):
            left = left - abs(divisor)
            times += 1

        return times if pos else -times
    
    def divide2(self, dividend: int, divisor: int) -> int:
        times = 0
        if dividend == 0:
            return 0
        if dividend == divisor:
            return 1
        pos = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        minV = (1 << 31) - 1
        if abs(divisor) == 1:
            if abs(dividend) >= (1 << 31) and pos:
                return minV
            else:
                return abs(dividend) if pos else -abs(dividend)
        n=abs(dividend)
        d=abs(divisor)
        while n >= d :
            p=0
            while n >= (d << (p + 1)):
                p += 1
            n -= (d << p)
            times += (1 << p)
        if times >= (1 << 31) and pos:
            return minV
        return times if pos else -times

