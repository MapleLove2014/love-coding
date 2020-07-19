class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result = []
        self.backtrack(result, '', digits)
        return result
        

    def backtrack(self, result, combination, digits):
        if not digits:
            result.append(combination)
        else:
            phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
            for letter in phone[digits[0]]:
                self.backtrack(result, combination + letter, digits[1:])

s = Solution()

print(s.letterCombinations('23'))
