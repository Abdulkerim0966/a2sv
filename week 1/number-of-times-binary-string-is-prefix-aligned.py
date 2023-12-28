class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        n=len(flips)
        
        lis=[0]*(n)
        
        pointer1=0
        pointer2=0
        ans=0
        k=0
        for i in flips:
            lis[i-1]=1

            if pointer2<i-1:
                pointer2=i-1


            if lis[pointer1]==1:

                while pointer1!=len(lis)-1 and lis[pointer1+1]==1 :
                    pointer1+=1
            if pointer1==k and pointer2==k:        
                ans+=1
            k+=1 
               
         
         
    
        return ans