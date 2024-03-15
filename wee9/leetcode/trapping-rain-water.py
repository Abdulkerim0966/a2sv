class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        count=0

        for i in range(len(height)):

            while stack and height [i] > stack[-1][0]:
                hi=stack.pop()[0]
                if stack:
                    minBound = min(height[i], stack[-1][0])
                    count += (i- stack[-1][1] - 1) * (minBound - hi)

    
            stack.append((height[i],i))
        
        return count


        # res, stack = 0, []
        
        # for r, rightBound in enumerate(height):
        #     while stack and height[stack[-1]] < rightBound:
        #         bar = height[stack.pop()]
        #         if stack:
        #             l, leftBound = stack[-1], height[stack[-1]]
        #             minBound = min(rightBound, leftBound)
        #             res += (r - l - 1) * (minBound - bar)
        #     stack.append(r)
        
        # return res
        