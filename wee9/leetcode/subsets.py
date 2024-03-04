class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current=[]
        ans=[]
        ans.append([])
        def backtrack(idx,li):

            if idx>=len(nums):
                
                return 
            

            for i in range(idx,len(nums)):
               
                current.append(nums[i])
                backtrack(i+1,nums[i+1:])
                ans.append(current.copy())
                current.pop()
            return ans
        return backtrack(0,nums)
       
        