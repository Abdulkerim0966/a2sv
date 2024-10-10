# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:


      loses={}
      for i in range(len(matches)):
          if matches[i][1] in loses:
              loses[matches[i][1]]+=1
          else :
              loses[matches[i][1]]=1
      print (loses)
      ans1=set()
      ans2=set()

      for i in range(len(matches)):
          if loses.get( matches[i][0],-1) ==-1:
              ans1.add(matches[i][0])
      for i in loses:
        if loses[i]==1:
          ans2.add(i)
      
      ans3=list(ans2)
      ans=list(ans1)
      ans.sort()
      ans3.sort()
    
      return [ans,ans3]
        

        
                

        