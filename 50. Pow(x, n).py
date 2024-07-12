# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if x == 1 or n == 1:
                return x
            if n == 0:
                return 1
            pos = True if n > 0 else False
            p2=pow(x, n // 2)
            if n % 2 == 0:
                return p2 * p2 if pos else 1 / (p2 * p2) 
            else:
                return x * p2 * p2 if pos else 1/ (x * p2 * p2)
        p=pow(x, abs(n))
        return p if n >= 0 else 1/p
    
s = Solution()
print(s.myPow(2.000, -2))
            