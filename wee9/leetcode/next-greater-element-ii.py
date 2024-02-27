class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        stack=[]
        for _ in range(2):
            for i in range(len(nums)):
                while stack and stack[-1][0]<nums[i]:
                    ans[stack[-1][1]]=nums[i]
                    stack.pop()
                stack.append([nums[i],i])
        return ans
                
        