class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in s:
            if i ==')':
                x=stack.pop()
                if x=='(':
                    stack.append(1)
                else:
                    ans=x 
                    while stack[-1] !='(':
                        x=stack.pop()
                        ans+=x
                    stack.pop()
                    stack.append(2*ans)
            else: 
                stack.append('(')
        return sum(stack)
        