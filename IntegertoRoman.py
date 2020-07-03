class Solution:
    def intToRoman(self, num: int) -> str:
        romans ={ v:k for k,v in {
            'I':  1, 
            'V':  5, 
            'IV': 4, 
            'X':  10, 
            'IX': 9, 
            'L':  50, 
            'XL': 40, 
            'C':  100, 
            'XC': 90, 
            'D':  500, 
            'CD': 400, 
            'M':  1000, 
            'CM': 900 

        }.items()}
        values = list(sorted(romans.keys()))
        if num == 0:
            return ''
        result = []
        value = 4000
        while num > 0:
            if num - value >= 0:
                result.append(romans[value])
                num -= value
            else:
                value = values.pop()

        return ''.join(result)


s = Solution()
print(s.intToRoman(3) == 'III')
print(s.intToRoman(4) == 'IV')
print(s.intToRoman(9) == 'IX')
print(s.intToRoman(58) == 'LVIII')
print(s.intToRoman(1994) == 'MCMXCIV')
