class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        d = {'(':')', '[':']', '{':'}'}

        for cc in s:
            if cc in d:
                stack.append(cc)
            elif len(stack) > 0 and d[stack[-1]] == cc:
                stack.pop()
            else:
                return False
        return len(stack) == 0
                
                
s = Solution()
print(s.isValid(")"))
print(s.isValid("()[]{}"))
print(s.isValid("()[{]}"))
print(s.isValid("{[]()}"))