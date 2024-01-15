class Solution:
    def balancedString(self, s: str) -> int:
        dect=Counter(s)
        n=len(s)/4
        left=0
        mi=float('inf')
        if max(dect.values())==n:
            return 0 
        for i in range(len(s)):
            dect[s[i]]-=1
            while max(dect.values())==n and left<i+1:
                mi=min(mi,i-left+1)
                dect[s[left]]+=1
                left+=1
            # if dect[s[i]]>n:
            
            # if max(dect.values())==n :
            #     mi=min(mi,i-left+1)
            
        return mi




        

        