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


