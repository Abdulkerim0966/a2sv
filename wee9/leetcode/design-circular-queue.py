class MyCircularQueue:

    def __init__(self, k: int):
        self.que=deque()
        self.size=k
        self.now=0
    def enQueue(self, value: int) -> bool:
        if self.now<self.size:
            self.que.append(value)
            self.now+=1
        
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.que:
            self.que.popleft()
            self.now-=1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.que:
            return self.que[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.que:
            return self.que[-1]
        else:
            return -1

        

    def isEmpty(self) -> bool:
        if self.que:
            return False
        else:
            return True
        

    def isFull(self) -> bool:
        return self.now==self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()