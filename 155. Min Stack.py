class MinStack:

    def __init__(self):
        self.stack = []
        self.minValeIndex = []

    def push(self, val: int) -> None:
        if not self.minValeIndex or self.stack[self.minValeIndex[-1]] >= val:
            self.minValeIndex.append(len(self.stack))
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.stack[self.minValeIndex[-1]]:
            self.minValeIndex.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.minValeIndex[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()