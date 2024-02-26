class Solution:
    def numberOfWays(self, s: str) -> int:
        psum=[0]*len(s)
        acc=0
        for i in range(len(s)):
            acc+=int(s[i])
            psum[i]=acc
 
        output=0
        for i in range(1,len(s)-1):
            if s[i]=='0':
                left=psum[i-1]
                right=psum[-1]-psum[i]
                
                output+=left*right
            else:
                left=(i+1)-psum[i] 
                right=(len(s) - i-1)-(psum[-1]-psum[i])     #(psum[i]+(len(s) - i-1))-psum[-1]
                output+=left*right

        return output     

           


        
        


        