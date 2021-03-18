class Solution:
    def generateParenthesis(self, n: int):
        def lookup(leftUsed, rightUsed, leftRemained, rightRemained, result, combine):
            if leftRemained == 0 and rightRemained == 0:
                result.add(combine)
                return
            if leftRemained == 0:
                for _ in range(rightRemained):
                    combine += ')'
                result.add(combine)
                return
            lookup(leftUsed + 1, rightUsed, leftRemained - 1, rightRemained, result, combine + '(')
            if rightUsed + 1 <= leftUsed:
                lookup(leftUsed, rightUsed + 1, leftRemained, rightRemained - 1, result, combine + ')')
        if n <= 0:
            return 0

        result = set()
        lookup(0, 0, n, n, result, '')
        return list(result)


s = Solution()
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))