class ATM:

    def __init__(self):
        self.dict=defaultdict(int)
    def deposit(self, banknotesCount: List[int]) -> None:
        self.dict['20']+=banknotesCount[0]
        self.dict['50']+=banknotesCount[1]
        self.dict['100']+=banknotesCount[2]
        self.dict['200']+=banknotesCount[3]
        self.dict['500']+=banknotesCount[4]
        
        

    def withdraw(self, amount: int) -> List[int]:
        noofnotes=[0,0,0,0,0]

        while amount>0:
            if amount>=500 and self.dict['500']>0:
                no=amount//500
                if no>self.dict['500']:
                    amount-=(500*self.dict['500'])
                    noofnotes[4]+=self.dict['500']
                    self.dict['500']=0
                else :   
                                        
                    self.dict['500']-=no
                    amount-=no*500
                    noofnotes[4]+=no
            elif amount>=200 and self.dict['200']>0:
                no=amount//200
                if no>self.dict['200']:
                    amount-=(200*self.dict['200'])
                    noofnotes[3]+=self.dict['200']
                    self.dict['200']=0
                else :   
                                        
                    self.dict['200']-=no
                    amount-=no*200
                    noofnotes[3]+=no
            elif amount>=100 and self.dict['100']>0:
                no=amount//100
                if no>self.dict['100']:
                    amount-=(100*self.dict['100'])
                    noofnotes[2]+=self.dict['100']
                    self.dict['100']=0
                else :   
                                        
                    self.dict['100']-=no
                    amount-=no*100
                    noofnotes[2]+=no
            elif amount>=50 and self.dict['50']>0:
                no=amount//50
                if no>self.dict['50']:
                    amount-=(50*self.dict['50'])
                    noofnotes[1]+=self.dict['50']
                    self.dict['50']=0
                else :   
                                        
                    self.dict['50']-=no
                    amount-=no*50
                    noofnotes[1]+=no
            elif amount>=20 and self.dict['20']>0:
                no=amount//20
                if no>self.dict['20']:
                    amount-=(20*self.dict['20'])
                    noofnotes[0]+=self.dict['20']
                    self.dict['20']=0
                else :   
                                        
                    self.dict['20']-=no
                    amount-=no*20
                    noofnotes[0]+=no
            else:
                self.dict['20']+=noofnotes[0]
                self.dict['50']+=noofnotes[1]
                self.dict['100']+=noofnotes[2]
                self.dict['200']+=noofnotes[3]
                self.dict['500']+=noofnotes[4]

                return [-1]
        
        return noofnotes

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)