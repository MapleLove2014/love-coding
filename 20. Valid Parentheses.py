# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


class Solution:


    def isValid2(self, s: str) -> bool:
        stack = []
        for cc in s:
            if cc == '(' or cc == '[' or cc == '{':
                stack.append(cc)
            else:
                if len(stack) == 0:
                    return False
                if cc == ')' and stack[-1] != '(':
                    return False
                if cc == ']' and stack[-1] != '[':
                    return False
                if cc == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return len(stack) == 0

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