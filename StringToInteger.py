NUMBER_DICT = { str(x) : x for x in range(10) }
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        startIndex = 0
        while startIndex < len(s):
            if s[startIndex] == ' ':
                startIndex += 1
            else:
                break
        if startIndex == len(s):
            return 0
        sign = {'-': -1, '+':1}
        numbers = { str(x) : x for x in range(10) }
        signNumber = 1
        if s[startIndex] in sign:
            signNumber = sign[s[startIndex]]
            startIndex += 1
        if startIndex == len(s) or s[startIndex] not in numbers:
            return 0
        result = 0
        while startIndex < len(s):
            if s[startIndex] not in numbers:
                break
            result = result * 10 + numbers[s[startIndex]]
            if result * signNumber > (1 << 31 ) - 1:
                return (1 << 31) - 1
            elif result * signNumber < -(1 << 31):
                return -( 1 << 31)
            startIndex += 1

        return result * signNumber

    def afterRefactor(self, s: str) -> int:
        integerStr = self.preprocess(s)
        if not integerStr:
            return 0
        if len(integerStr) == 1 and self.isSign(integerStr[0]):
            return 0
        
        result = 0
        startIndex = 1 if self.isSign(integerStr[0]) else 0
        while startIndex < len(integerStr):
            result = result * 10 + NUMBER_DICT[integerStr[startIndex]]
            overflow, bound = self.boundOverflow(self.getSignNumber(integerStr[0]), result)
            if overflow:
                return bound
            startIndex += 1
        return result * self.getSignNumber(integerStr[0])


    def preprocess(self, s):
        return self.processTail(self.processHeader(s))

    def processHeader(self, s):
        if not s:
            return ''
        for i in range(len(s)):
            if s[i] != ' ':
                return s[i:]
        return ''

    def processTail(self, s):
        if not s:
            return ''
        for i in range(len(s)):
            if i == 0:
                if not self.isSign(s[i]) and not self.isNumber(s[i]):
                    return ''
            elif not self.isNumber(s[i]):
                return s[:i]
        return s

    def isNumber(self, c):
        return c in NUMBER_DICT

    def isSign(self, c):
        return c == '-' or c == '+'

    def getSignNumber(self, c):
        return -1 if c == '-' else 1
    
    def boundOverflow(self, signNumber, absoluteValue):
        if self.upperBoundOverflow(signNumber * absoluteValue):
            return (True, (1 << 31 ) - 1)
        if self.lowerBoundOverflow(signNumber * absoluteValue):
            return (True, -(1 << 31))
        return (False, None)

    def upperBoundOverflow(self, integer):
        return integer > (1 << 31 ) - 1

    def lowerBoundOverflow(self, integer):
        return integer < -(1 << 31)

s = Solution()
print(s.myAtoi('42') == 42)
print(s.myAtoi('   -42') == -42)
print(s.myAtoi('4193 with words') == 4193)
print(s.myAtoi('words and 987') == 0)
print(s.myAtoi('-91283472332') == -2147483648)

print('refactor result')

print(s.afterRefactor('42') == 42)
print(s.afterRefactor('   -42') == -42)
print(s.afterRefactor('4193 with words') == 4193)
print(s.afterRefactor('words and 987') == 0)
print(s.afterRefactor('-91283472332') == -2147483648)
