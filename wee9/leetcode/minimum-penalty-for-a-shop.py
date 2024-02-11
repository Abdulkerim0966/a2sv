class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pe=[]
        count=0

        for j in range (len(customers)):
            if customers[j]=="Y":
                count+=1
       
        pe.append(count)

        for i in range (len(customers)):
            if customers[i]=="Y":
                count-=1
                pe.append(count)
            else:
                count+=1
                pe.append(count)  

        mi=min(pe)
        pe.index(mi)
        return pe.index(mi) 
    
            

                
                
    