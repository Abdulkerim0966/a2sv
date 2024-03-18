class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        heights.append(-1)
        mini=0
        for i in range(len(heights)):
            count=0
            

            while stack and stack[-1][0] >= heights[i]:
                x=stack.pop()
                count+=x[1]
                mini = max(mini,x[0]*(count))

            stack.append([heights[i],count+1])
        return mini
        

        
        