class Solution:
    def minimumSum(self, num: int) -> int:
        s=list(str(num))
        s.sort()
        print (s)
        
        return(int(s[0]+s[3])+int(s[1]+s[2]))
        

        