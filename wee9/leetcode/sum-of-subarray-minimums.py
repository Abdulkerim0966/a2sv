class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans=[1]*len(arr)
        stack=[]

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                ans[stack[-1]] *= (i - stack[-1])
                stack.pop()

            stack.append(i)


        for i in range(len(stack)):

            ans[stack[i]] *= ((stack[-1] - stack[i])+1)
        
        print(ans) 
        stack=[]
        ans.reverse()
        arr.reverse()

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                ans[stack[-1]] *= (i - stack[-1])
                stack.pop()

            stack.append(i)

        print(ans)
        for i in range(len(stack)):

            ans[stack[i]] *= ((stack[-1] - stack[i])+1)

        
        for i in range(len(arr)):
            ans[i] *= arr[i]
        
        


        return sum(ans) % (10 ** 9 + 7)

        

        