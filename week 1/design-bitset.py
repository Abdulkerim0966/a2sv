class Bitset:

    def __init__(self, size: int):
        self.countbit1=0
        self.list=[0 for i in range(size)]
        self.flip_no=0
        self.size=size

        

    def fix(self, idx: int) -> None:
        if self.flip_no%2==1 and self.list[idx]==1:
            self.list[idx]=0
            self.countbit1-=1
        elif self.flip_no%2==0 and self.list[idx]==0:
            self.list[idx]=1
            self.countbit1+=1
        

    def unfix(self, idx: int) -> None:
        if self.flip_no%2==1 and self.list[idx]==0:
            self.list[idx]=1
            self.countbit1+=1
        elif self.flip_no%2==0 and self.list[idx]==1:
            self.list[idx]=0 
            self.countbit1-=1   
        
    def flip(self) -> None:
        self.flip_no+=1

    def all(self) -> bool:
        if self.flip_no%2==0:
            if self.countbit1==self.size:
                return True
            else:
                return False
        else:
            if self.countbit1==0:
                return True
            else:
                return False            
        

    def one(self) -> bool:
        if self.flip_no%2==0:
            if self.countbit1>0:
                return True
            else:
                return False
        else:
            if self.countbit1<self.size:
                return True
            else:
                return False  
        

    def count(self) -> int:
        if self.flip_no%2==0:
            return self.countbit1
        else:
            return self.size-self.countbit1  

    def toString(self) -> str:
        if self.flip_no%2==0:
            return "".join(map(str,self.list))
            
        elif self.flip_no%2==1:
            print(self.flip_no)
            print(self.list)
            listtoprint=[]
            for i in range(self.size):
                if self.list[i] == 0:
                    listtoprint.append(1) 
                else:
                    listtoprint.append(0)
            return"".join(map(str,listtoprint))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()