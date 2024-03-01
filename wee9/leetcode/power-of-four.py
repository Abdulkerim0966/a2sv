class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def cal(h):
            if h<4:
                return h

            return cal(h/4)
        x=cal(n)
  
        return x==1  
        