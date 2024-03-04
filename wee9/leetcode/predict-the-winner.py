class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total=0
        def turninng(num):
  
            if len(num)==1 :
                
                return num[0]
    
                
            total=max (num[0]-turninng(num [1:len(num)]),num[-1] -turninng(num[:len(num)-1]))

            return total
        return turninng((nums))>=0
       


        