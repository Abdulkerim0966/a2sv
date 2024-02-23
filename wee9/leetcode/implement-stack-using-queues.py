class MyStack:

    def __init__(self):
        self.que=deque()
        

    def push(self, x: int) -> None:
        self.que.append(x)
        

    def pop(self) -> int:
        x=self.que.pop()
        return x

    def top(self) -> int:
        x=self.que.pop()
        self.que.append(x)
        return x

        

    def empty(self) -> bool:
        
        return True if len(self.que)==0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()