class MinStack:

    def __init__(self):
        self.stack=[]
        self.mi=deque()
        self.m=float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.m >val:
            self.mi.appendleft(val)
            self.m=val
        else:
            self.mi .append(val)

    def pop(self) -> None:
        if self.m ==self.stack[-1] and self.mi[-1]!=self.stack[-1]:
            self.mi.popleft()
            self.m=self.mi[0]
        else:
            self.mi .pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mi[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()