class Robot:

    def __init__(self, width: int, height: int):
        self.row=height-1
        self.colomn=width-1
        self.mo=[]
        self.f1=True
        self.position=0
        for i in range(self.colomn+1):
            self.mo.append((0,i))
        for i in range(1,self.row+1):
            self.mo.append((i,self.colomn))
        for i in range(self.colomn-1,-1,-1):
            self.mo.append((self.row,i))
        for i in range(self.row-1,0,-1):
            self.mo.append((i,0))
        self.size=len(self.mo)
        print(self.mo)
        

    def step(self, num: int) -> None:
        self.f1=False
        uni_step=num%self.size
        self.position=((self.position + uni_step)% self.size)
     

    def getPos(self) -> List[int]:
        print(self.position)
        return [self.mo[self.position][1],self.mo[self.position][0]]
        

    def getDir(self) -> str:
        if self.mo[self.position]==(0,0) and self.f1==True:
            return'East'
        elif self.mo[self.position][0]==0 and self.mo[self.position][1]!=0 :
            return 'East'
        elif self.mo[self.position][0]!=0 and self.mo[self.position][1]==self.colomn :
            return'North' 
        elif self.mo[self.position][0]==self.row and self.mo[self.position][1]!=self.colomn :
            return 'West'
        else:
            return 'South'
            



        
        
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()