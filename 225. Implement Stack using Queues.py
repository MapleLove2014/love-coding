class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        q = self.q1 if not self.q2 else self.q2
        q.insert(0, x)
        

    def pop(self) -> int:
        q = self.q1
        b = self.q2
        if not self.q1:
            q = self.q2
            b = self.q1
        
        l = len(q)
        for _ in range(l-1, 0, -1):
            b.insert(0, q.pop())
        return q.pop()

    def top(self) -> int:
        q = self.q1 if not self.q2 else self.q2
        return q[0]
        

    def empty(self) -> bool:
        return not self.q1 and not self.q2
        

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top()) #// return 2
print(myStack.pop()) # // return 2
print(myStack.empty()) #// return False