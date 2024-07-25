class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        n = []
        ops = {
            "+": lambda n1,n2: n1 + n2,
            "-": lambda n1,n2: n1-n2,
            "*": lambda n1,n2: n1*n2,
            "/": lambda n1,n2: int(n1/n2)
        }
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                n2 = n.pop()
                n1 = n.pop()
                n.append(ops[t](n1, n2))
            else:
                n.append(int(t))
        return n.pop()
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))

