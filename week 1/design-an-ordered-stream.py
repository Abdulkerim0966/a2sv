class OrderedStream:

    def __init__(self, n: int):
        self.list=[""]*n
        
        
        self.begin=0

    def insert(self, idKey: int, value: str) -> List[str]:
        print(self.begin)
        self.list[idKey-1]=value    
        if self.begin==idKey-1:
            ans=[]
            while self.begin<len(self.list) and self.list[self.begin]!=""  :
                ans.append(self.list[self.begin])
                self.begin+=1
            
            return ans
        else:
            return []

           

         


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)