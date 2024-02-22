class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        li=list(path.split('/'))
        print(li)
        for i in range(len(li)):
            if li[i]=="" or li[i]=='.' :
                continue
            elif li[i]=='..':
                if stack:
                    stack.pop() 
            else:
                stack.append(li[i])
        print(stack,li)

        return '/'+'/'.join(stack)
                
        