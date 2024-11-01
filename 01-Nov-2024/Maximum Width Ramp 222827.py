# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans =0
        stack =[]

        stack.append((nums[0],0))
        for i in range(1,len(nums)):
            if stack[-1][0]>nums[i]:
                stack.append((nums[i],i))
            else:
                j =len(stack)-1
                while j >=0 and stack[j][0] <=nums[i]:
                    ans =max(ans,i-stack[j][1])
                    j-=1
        return ans
        
        