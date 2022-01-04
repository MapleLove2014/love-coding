class Solution:
    def plusOne(self, digits):
        
        if not digits or len(digits) == 0:
            return 1
        # [1,2,3]
        result = [0] * (len(digits)  + 1)
        result[-1] = 1
        carr = 0
        for i in range(len(digits) - 1, -1, -1):
            s = result[i + 1] + digits[i] + carr
            carr = s // 10
            result[i + 1] = s % 10
        result[0] = carr

        return result if result[0] != 0 else result[1:]


s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([1]))
print(s.plusOne([9]))

