class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 3:
            return True if n > 0 else False
        for t in [2,3,5]:
            if n % t == 0:
                return self.isUgly(n // t)
        return False
            
            
s = Solution()
print(s.isUgly(14))
print(s.isUgly(-10))
print(s.isUgly(25))