class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        re = True
        dect={ ")" : "(", "]":"[",  "}":"{"  }
    
        for i in range (len(s)):
            if s[i] not in dect:
                stack.append(s[i])
               
            elif stack and stack[-1]==dect[s[i]]:
                stack.pop()
                
            else:
                re = False
            
        if re==False or len(stack) != 0 :
            re = False
        return re