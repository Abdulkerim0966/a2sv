class Solution:
    def longestPalindrome(self, s: str) -> int:
        dect=Counter(s)
        ans=0
        flag=False
        for i in dect:
            if dect[i]%2==0:
                ans+=(dect[i])
            else:
                if dect[i]>2:
                    ans+=(dect[i]-1)
                    dect[i]-=(dect[i]-1)
                    
                if flag==False:
                    ans+=1
                    flag=True
        return ans
        