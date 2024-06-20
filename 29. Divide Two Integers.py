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