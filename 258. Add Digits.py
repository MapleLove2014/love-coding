class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            inner = num
            s = 0
            while inner > 0:
                s += (inner % 10)
                inner = inner // 10
            num = s
        return num
    def addDigits2(self, num: int) -> int:
        while num >= 10:
            n = 0
            while num > 0:
                n += (num % 10)
                num = num // 10
            num = n
        return num


