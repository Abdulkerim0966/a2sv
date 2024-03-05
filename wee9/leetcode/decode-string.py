class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        ans=[]
        for i in range(len(s)):
            stack.append(s[i])
            if stack[-1]==']':
                stack.pop()
                temp=[]
                while stack[-1]!='[':
                    temp.append(stack.pop())
                stack.pop()
                temp.reverse()
               
                n=stack.pop()
                while stack and stack[-1].isnumeric():
                    n+=stack.pop()
             
                n=int(n[::-1])
          
                a=''.join(temp)
                stack.append(a*n)
        return ''.join (stack)



            
        
        
                
         
        