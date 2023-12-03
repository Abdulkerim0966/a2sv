class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        so=sorted(words,key=lambda x: len(x))
        ma=len(so[len(so)-1])
       
        ans=[]
        for i in range(ma):
            s=""
            for j in range (len(words)):

                if len(words[j])>i:
                  
                    s+=words[j][i]
                else:
                    s+=" "
            
            ans.append(s.rstrip())
        return ans
            
