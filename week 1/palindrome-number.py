class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        re=True
        left=0
        right=len(x)-1
        while left<right:
            if x[left] != x[right]:
                re=False
                
                break
            else:
                left+=1
                right-=1
        return re



    
    

        