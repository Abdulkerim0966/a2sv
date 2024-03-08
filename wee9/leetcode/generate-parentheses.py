class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s) -> bool:
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



        bucket=[]
        ans=[]
        num=['(',')']
        def backtrack(idx):
            
            if len(bucket)==2*n and isValid(bucket):
               
                ans.append(''.join(bucket))
                return 
            elif len(bucket)==2*n:
                return
           

            for i in range(2):
                         
                bucket.append(num[i])
                backtrack(i+1)
                bucket.pop()
                
        backtrack(2*n)

        return ans