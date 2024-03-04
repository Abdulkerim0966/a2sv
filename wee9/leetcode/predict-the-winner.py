class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # total=0
        # def turninng(num,turn,total):
  
        
        #     if len(num)<=2  and turn==2:
        #         total-=max(num)
        #         # print(num,total)
        #         return total
        #     if len(num)==1 and turn==1:
                
        #         return total
            
        #     if turn==2:
    
        #         total-=min(turninng(num[:len(num)-1],1,total),turninng(num[1:len(num)],1,total))
   
        #         return total
                
                
                    
        #     else:
             
                
        #         return max (turninng (num [1:len(num)],2,total),  turninng(num[:len(num)-1],2,total))
        # ans=turninng(nums,1,total)
         
        # return( (sum(nums)-ans)<=ans)
        def helper(i, j):
            if i == j:
                return nums[i]

            score = max(nums[j] - helper(i, j-1), nums[i] - helper(i+1, j))
        
            return score
            
             
        return helper(0, len(nums)-1) >= 0


        