class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def cal (h):
            if  h<3:

                return h
            
            return cal(h/3)
        x=cal(n)
      
        return x==1

        