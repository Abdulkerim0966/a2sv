class Solution:

    def minWindow(self, s: str, t: str) -> str:
        dect1=Counter(t)
        dect=Counter()
        to=sum(dect1.values())
        def compare(dect2):
            for c in dect1:
                if dect1[c]>dect2[c]:
                    return False
            return True
        

        left=0
        ans=""
        mi=float('inf')
        ch=0
        
        for i in range(len(s)):
            if s[i] in t:
                dect[s[i]]+=1
                ch+=1
            if ch>=to:
                print(ch)
                if compare(dect)==True:
                
                    while left<len(s) and ( compare(dect)==True ):
                        if mi>i-left:
                            ans=s[left:i+1]
                            mi=i-left
          
                        if s[left] in t:
                            dect[s[left]]-=1
                            ch-=1
                
                        left+=1
                print(ch,left)
              
        return ans
                        
           
                



        