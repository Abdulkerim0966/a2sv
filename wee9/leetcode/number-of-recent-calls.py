class RecentCounter:

    def __init__(self):
        self.que=deque()
        self.no=0
        

    def ping(self, t: int) -> int:
        self.que.append(t)
        self.no+=1
        while t-self.que[0]>3000:
            self.que.popleft()
            self.no-=1
        return self.no


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)