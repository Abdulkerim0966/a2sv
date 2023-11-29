class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        x=strs[0]
        bre=True
        for i in range (len(x)):
            for j in range (len(strs)):
                y=strs[j]
                if i==len(y) or x[i]!=y[i]:
                    bre=False
                    break
                else:
                    continue
            if  bre==False:
                break
            else :
                ans.append(x[i])
        re="".join(ans)
        return re




           
       
                
                
        