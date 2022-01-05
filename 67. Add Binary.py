class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result  = [0] * (max(len(a), len(b)) + 1)
        carr = 0
        resultL = max(len(a), len(b)) + 1

        a = ("0" * (resultL - len(a))) + a
        b = ("0" * (resultL - len(b))) + b
        
        for i in range(resultL - 1, -1 , -1):
            s = result[i] + int(a[i]) + int(b[i]) + carr
            carr = s // 2
            result[i] = s % 2
        return "".join(map(str, result[1:])) if result[0] == 0 else "".join(map(str, result))


s = Solution()
#print(s.addBinary("11", "1"))
#print(s.addBinary("1010", "1011"))
print(s.addBinary("0", "0"))
