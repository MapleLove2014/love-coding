class Solution:
    def romanToInteger(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'IV': 4,
            'X': 10,
            'IX' : 9,
            'L': 50,
            'XL': 40,
            'C': 100,
            'XC': 90,
            'D': 500,
            'CD': 400,
            'M': 1000,
            'CM': 900
        }
        if not s:
            return 0
        i = 0
        result = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in romans:
                result += romans[s[i:i+2]]
                i += 2
            else:
                result += romans[s[i]]
                i += 1

        return result

s = Solution()
print(s.romanToInteger('III') == 3)
print(s.romanToInteger('IV') == 4)
print(s.romanToInteger('IX') == 9)
print(s.romanToInteger('MCMXCIV') == 1994)
