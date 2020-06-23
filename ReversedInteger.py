class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 10:
            return x
        
        unsignedX = int(str(abs(x))[::-1])
        result = unsignedX if x >= 0 else unsignedX * -1
        if result > (1 << 31) - 1 or result < -(1 << 31):
            return 0
        return result

    def reverse2(self, x: int) -> int:       
        if abs(x) < 10:
            return x
        result = 0
        modNumber = 10
        absX = abs(x)
        while absX > 0:
            result = result * 10 + (absX % modNumber)
            absX //= modNumber
            if result > (1 << 31) - 1 or result < -(1 << 31):
                return 0
        return result if x >= 0 else -1 * result
    
s = Solution()
print(s.reverse2(-123))